# Generated by Django 3.2.9 on 2021-11-10 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211110_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='has_sizez',
            new_name='has_sizes',
        ),
    ]
