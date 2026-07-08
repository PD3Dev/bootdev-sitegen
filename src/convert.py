from htmlnode import *
from textnode import *
from blocks import *
import re
import os

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    result_nodes = []

    for node in old_nodes:
        new_nodes = []
        if node.text_type != TextType.PLAIN:
            result_nodes.append(node)
            continue

        split = node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise Exception('Wrong Markdown syntax. Check delimiters.')
        for i in range(len(split)):
            if i % 2 == 0:
                if split[i] != '':
                    new_nodes.append(TextNode(split[i], TextType.PLAIN))
                else:
                    continue
            else:
                if split[i] != '':
                    new_nodes.append(TextNode(split[i], text_type))
                else:
                    continue

        result_nodes.extend(new_nodes)

    return result_nodes

def extract_markdown_images(text):
    alt_text = re.findall(r"\!\[(.*?)\]", text)
    img_url = re.findall(r"\!\[.*?\]\((.*?)\)", text)
    images = []
    if len(alt_text) != len(img_url):
        raise Exception('Image Markup syntax invalid. Check alt text link combinations.')
    for i in range(len(alt_text)):
        images.append((alt_text[i], img_url[i]))
    return images

def extract_markdown_links(text):
    anchor_text = re.findall(r"\[(.*?)\]", text)
    link_url = re.findall(r"\[.*?\]\((.*?)\)", text)
    links = []
    if len(anchor_text) != len(link_url):
        raise Exception('Link Markup syntax invalid. Check alt text link combinations.')
    for i in range(len(anchor_text)):
        links.append((anchor_text[i], link_url[i]))
    return links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            result_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        new_nodes = []
        segments = [node.text]
        for image in images:
            if image[1] == '':
                raise Exception('Invalid Markdown syntax. All one or more images do not have a URL')
            segments = segments[-1].split(f'![{image[0]}]({image[1]})', 1)
            if segments[0] != '':
                new_nodes.append(TextNode(segments[0], TextType.PLAIN))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if segments[-1] != '':
            new_nodes.append(TextNode(segments[-1], TextType.PLAIN))
        result_nodes.extend(new_nodes)


    return result_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            result_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        new_nodes = []
        segments = [node.text]
        for link in links:
            segments = segments[-1].split(f'[{link[0]}]({link[1]})', 1)
            if link[1] == '':
                raise Exception('Invalid Markdown syntax. All one or more links do not have a URL')
            if segments[0] != '':
                new_nodes.append(TextNode(segments[0], TextType.PLAIN))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        if segments[-1] != '':
            new_nodes.append(TextNode(segments[-1], TextType.PLAIN))
        result_nodes.extend(new_nodes)

    return result_nodes

def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.PLAIN)

    bold = split_nodes_delimiter([initial_node], '**', TextType.BOLD)
    italic = split_nodes_delimiter(bold, '_', TextType.ITALIC)
    code = split_nodes_delimiter(italic, '`', TextType.CODE)
    images = split_nodes_image(code)
    links = split_nodes_link(images)

    return links

def markdown_to_blocks(markdown):
    segments = markdown.split('\n\n')
    result = []
    for i in range(len(segments)):
        segments[i] = segments[i].strip()
        if segments[i] != '':
            result.append(segments[i])
    return result


def get_heading_tag(heading):
    if heading.startswith('# '):
        return 'h1'
    if heading.startswith('## '):
        return 'h2'
    if heading.startswith('### '):
        return 'h3'
    if heading.startswith('#### '):
        return 'h4'
    if heading.startswith('##### '):
        return 'h5'
    if heading.startswith('###### '):
        return 'h6'

def heading_to_parent_node(md_heading):
    split = md_heading.split('# ')
    stripped = split[-1]
    children = text_to_children(stripped)
    return ParentNode(get_heading_tag(md_heading), children)

def paragraph_to_parent_node(md_paragraph):
    md_paragraph = md_paragraph.replace('\n', ' ')
    children = text_to_children(md_paragraph)
    return ParentNode('p', children)

def quote_to_parent_node(md_quote):
    text = md_quote.replace('>', '')
    text = text.lstrip()
    children = text_to_children(text)
    return ParentNode('blockquote', children)

def ul_to_parent_node(md_ul):
    ul_children = []
    list_items = md_ul.split('\n')
    for item in list_items:
        item = item[2:]
        item_children = text_to_children(item)
        ul_children.append(ParentNode('li', item_children))
    return ParentNode('ul', ul_children)

def ol_to_parent_node(md_ul):
    ol_children = []
    list_items = md_ul.split('\n')
    for item in list_items:
        split = item.split('.', 1)
        item = split[1]
        item = item.strip()
        item_children = text_to_children(item)
        ol_children.append(ParentNode('li', item_children))
    return ParentNode('ol', ol_children)

def code_to_parent_node(md_code):
    text = md_code.strip('`')
    text = text.lstrip()
    code_text_node = TextNode(text, TextType.CODE)
    child_html_node = [text_node_to_html_node(code_text_node)]
    return ParentNode('pre', child_html_node)

def text_to_children(text):
    tn_children = text_to_textnodes(text)
    html_children = []

    for tn in tn_children:
        child = text_node_to_html_node(tn)
        html_children.append(child)
    return html_children


def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in md_blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            html_nodes.append(heading_to_parent_node(block))
        if block_to_block_type(block) == BlockType.CODE:
            html_nodes.append(code_to_parent_node(block))
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            html_nodes.append(paragraph_to_parent_node(block))
        if block_to_block_type(block) == BlockType.QUOTE:
            html_nodes.append(quote_to_parent_node(block))
        if block_to_block_type(block) == BlockType.ORDERED_LIST:
            html_nodes.append(ol_to_parent_node(block))
        if block_to_block_type(block) == BlockType.UNORDERED_LIST:
            html_nodes.append(ul_to_parent_node(block))
    return ParentNode('div', html_nodes)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith('# '):
            return block.strip('# ')
    raise Exception('No title found')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}.')
#Read markdown and template and store contents in variables.
    with open(from_path) as markdown:
        md_content = markdown.read()

    with open(template_path) as template:
        temp_content = template.read()

#Create the full HTML str from the markdown content and extract the page title.
    html_node = markdown_to_html_node(md_content)
    html_str = html_node.to_html()
    page_title = extract_title(md_content)

#Replace title and html content in the template file and save it.
    temp_content = temp_content.replace('{{ Title }}', page_title)
    temp_content = temp_content.replace('{{ Content }}', html_str)

#Write the final HTML file with updated template content.
    with open(dest_path, mode='w') as html_file:
        html_file.write(temp_content)

def generate_pages_recursive(from_path, template_path, dest_path, basepath):
#List content of current directory
    content = os.listdir(from_path)

#Crawl through content to check for .md files
    for item in content:
        item_path = f'{from_path}/{item}'
        if os.path.isfile(item_path):
            if item.endswith('.md'):
                with open(item_path) as markdown:
                    md_content = markdown.read()

                with open(template_path) as template:
                    temp_content = template.read()

            #Create the full HTML str from the markdown content and extract the page title.
                html_node = markdown_to_html_node(md_content)
                html_str = html_node.to_html()
                page_title = extract_title(md_content)

            #Replace title and html content in the template file and save it.
                temp_content = temp_content.replace('{{ Title }}', page_title)
                temp_content = temp_content.replace('{{ Content }}', html_str)
                temp_content = temp_content.replace('href="/', 'href="{basepath}')
                temp_content = temp_content.replace('src="/', 'src="{basepath}')

            #Write the final HTML file with updated template content.
                filename = item.strip('.md')
                filename += '.html'
                with open(f'{dest_path}/{filename}', mode='w') as html_file:
                    html_file.write(temp_content)
        else:
#The item is a folder. Create new from and dest paths and recursivgely call the function.
            nested_folder_path = f'{from_path}/{item}'
            new_dest_path = f'{dest_path}/{item}'
            os.mkdir(new_dest_path)
            generate_pages_recursive(nested_folder_path, template_path, new_dest_path, basepath)
