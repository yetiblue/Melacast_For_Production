# Generated by Django 3.0.6 on 2021-02-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0011_auto_20210211_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='genre',
            field=models.CharField(default='null', max_length=100),
        ),
    ]