# Generated by Django 3.0.6 on 2021-02-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0013_auto_20210215_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='education_background',
            field=models.TextField(default='no url', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='actors',
            name='pronouns',
            field=models.TextField(default='no url', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='actors',
            name='union_status',
            field=models.TextField(default='no url', max_length=150, null=True),
        ),
    ]
