from htmlnode import *
from textnode import *
import re

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
