# Generated by Django 2.2.20 on 2021-11-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20211111_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.CharField(choices=[('remote', 'remote'), ('full time', 'full time')], default=False, max_length=20),
        ),
    ]
