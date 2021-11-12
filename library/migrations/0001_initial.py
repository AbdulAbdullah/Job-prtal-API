# Generated by Django 2.2.20 on 2021-11-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('isbn', models.CharField(blank=True, max_length=200)),
                ('publisher', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
