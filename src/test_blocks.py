import unittest
from blocks import *
from blocks import block_to_block_type
from blocks import BlockType

class TestDelimiterSplit(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = '# This is a heading'
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_block_to_block_type_code(self):
        block = '''```
>This is a code block.
>And it consists of two lines.```'''
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )

    def test_block_to_block_type_quote(self):
        block = '''>This is a quote
>And here is another line
>And another one
>And a last one'''
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )

    def test_block_to_block_type_ordered(self):
        block = '''- This is a quote
- And here is another line
- And another one
- And a last one'''
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )

    def test_block_to_block_type_paragraph(self):
        block = 'This is a paragraph.'
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )
if __name__ == "__main__":
    unittest.main()
