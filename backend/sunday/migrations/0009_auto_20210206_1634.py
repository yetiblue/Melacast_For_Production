# Generated by Django 3.0.6 on 2021-02-06 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0008_auto_20210206_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actors',
            name='post_production_roles',
        ),
        migrations.RemoveField(
            model_name='actors',
            name='production_roles',
        ),
    ]