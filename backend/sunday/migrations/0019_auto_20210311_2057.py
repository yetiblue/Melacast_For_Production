# Generated by Django 3.0.6 on 2021-03-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0018_stripecustomer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actors',
            name='union_status',
        ),
        migrations.AddField(
            model_name='actors',
            name='union',
            field=models.TextField(default='Missing Field', max_length=150, null=True),
        ),
    ]