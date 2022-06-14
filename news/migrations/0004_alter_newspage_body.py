# Generated by Django 4.0.4 on 2022-05-18 22:25

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newspagetag_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('intro', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))], icon='image', label='Aligned image')), ('embed', wagtail.blocks.StructBlock([('you_tube_embed', wagtail.blocks.CharBlock(help_text='Insert the embed code e.g Pha7WiAuhw4 the part that follows https://youtu.be/', required=False))], icon='code')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))], icon='code', label='Raw HTML'))], use_json_field=True),
        ),
    ]