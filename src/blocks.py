from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered list'
    ORDERED_LIST = 'ordered list'

def block_to_block_type(block):
    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    if block.startswith('```\n') and block.endswith('```'):
        return BlockType.CODE
    if block.startswith('>'):
        segments = block.split('\n')
        if all(segment.startswith('>') for segment in segments):
            return BlockType.QUOTE
    if block.startswith('- '):
        segments = block.split('\n')
        if all(segment.startswith('- ') for segment in segments):
            return BlockType.UNORDERED_LIST
    if block.startswith('1.'):
        segments = block.split('\n')
        check = True
        for i in range(len(segments)):
            num = i + 1
            if not segments[i].startswith(f'{num}.'):
                check = False
                break
        if check:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


