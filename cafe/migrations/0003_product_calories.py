# Generated by Django 3.2.8 on 2021-10-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_auto_20211023_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='calories',
            field=models.PositiveIntegerField(default=230),
            preserve_default=False,
        ),
    ]
