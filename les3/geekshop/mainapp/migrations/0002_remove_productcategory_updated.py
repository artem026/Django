# Generated by Django 3.2.3 on 2021-06-03 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='updated',
        ),
    ]
