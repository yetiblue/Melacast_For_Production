# Generated by Django 3.0.6 on 2021-06-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0051_actors_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='tagline',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='memberlistings',
            name='tagline',
            field=models.CharField(max_length=255, null=True),
        ),
    ]