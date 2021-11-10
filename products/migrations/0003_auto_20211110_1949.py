# Generated by Django 3.2.9 on 2021-11-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='has_sizez',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
