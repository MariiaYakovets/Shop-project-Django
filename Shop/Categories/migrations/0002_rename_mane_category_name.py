# Generated by Django 5.0.7 on 2024-07-31 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='mane',
            new_name='name',
        ),
    ]
