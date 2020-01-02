"""Streamfields live in here."""

from wagtail.core import blocks
from wagtail.contrib.table_block.blocks import TableBlock

class StreamTableBlock(blocks.StructBlock):
    """Table Block"""
    table = TableBlock()
    
    class Meta:  # noqa
        template = "streams/table_block.html"
        icon = "table"
        label = "Table"


class TableHead(blocks.StructBlock):
    table_head_text = blocks.ListBlock(blocks.CharBlock(max_length=120))

class TableRow(blocks.StructBlock):
    table_row_text = blocks.ListBlock(blocks.CharBlock(max_length=120))

class TableBlock(blocks.StructBlock):
    caption_text = blocks.CharBlock(max_length=120)
    table_head = TableHead()
    table_rows = blocks.ListBlock(TableRow())

    class Meta:
        template = 'streams/table.html'
        icon = "table"
        label = "Simple Table"

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"

# class CardBlock(blocks.StructBlock):
#     """files from filemanager and nothing else."""

#     title = blocks.CharBlock(required=True, help_text="Add your title")
#     cards = blocks.ListBlock{
#         blocks.StructBlock([
#             ("image", Image)
#         ])
#     }
