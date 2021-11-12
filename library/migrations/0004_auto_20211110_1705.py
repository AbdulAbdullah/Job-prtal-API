# Generated by Django 2.2.20 on 2021-11-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20211110_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tags',
        ),
        migrations.AddField(
            model_name='book',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
