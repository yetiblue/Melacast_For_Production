# Generated by Django 3.0.6 on 2021-04-07 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0036_filmroles_date_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='date_submitted',
            field=models.CharField(max_length=200, null=True),
        ),
    ]