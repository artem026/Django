# Generated by Django 3.2.3 on 2021-06-17 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210607_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]