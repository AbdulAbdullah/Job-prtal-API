# Generated by Django 2.2.20 on 2021-11-11 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20211110_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.CharField(choices=[('remote', 'remote'), ('full time', 'full time')], default=None, max_length=20),
        ),
    ]
