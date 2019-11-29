# Generated by Django 2.2.7 on 2019-11-29 15:06

from django.db import migrations
import streams.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0014_kbindexpage_banner_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kbpage',
            name='content',
            field=wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichtextBlock()), ('simple_richtext', streams.blocks.SimpleRichtextBlock()), ('table_block', wagtail.core.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock())]))], blank=True, null=True),
        ),
    ]
