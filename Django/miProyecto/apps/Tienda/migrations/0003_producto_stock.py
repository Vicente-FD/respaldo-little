# Generated by Django 4.2.1 on 2023-06-27 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]