# Generated by Django 2.2.20 on 2021-11-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20211112_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('qualification', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Book',
            new_name='Job',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
