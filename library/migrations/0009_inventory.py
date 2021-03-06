# Generated by Django 2.2.20 on 2021-11-12 05:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20211111_0530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('item_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('image', models.URLField()),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
