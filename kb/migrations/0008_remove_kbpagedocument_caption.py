# Generated by Django 2.2.4 on 2019-08-30 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0007_auto_20190830_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kbpagedocument',
            name='caption',
        ),
    ]
