# Generated by Django 4.2 on 2023-04-27 22:44

from django.db import migrations, models
import lists.models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.TextField(default=None, verbose_name=lists.models.List),
        ),
    ]
