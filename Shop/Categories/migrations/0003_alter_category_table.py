# Generated by Django 5.0.7 on 2024-07-31 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0002_rename_mane_category_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Categories',
        ),
    ]