# Generated by Django 3.0.6 on 2021-04-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0044_auto_20210428_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='poster',
            field=models.TextField(default='', max_length=300),
        ),
    ]