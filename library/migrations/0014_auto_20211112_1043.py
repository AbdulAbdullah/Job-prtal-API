# Generated by Django 2.2.20 on 2021-11-12 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20211112_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='tagiii',
            new_name='profession',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='tag',
            new_name='type',
        ),
    ]
