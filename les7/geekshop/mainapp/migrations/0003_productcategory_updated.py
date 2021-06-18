# Generated by Django 3.2.3 on 2021-06-03 23:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_productcategory_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]