# Generated by Django 3.0.6 on 2021-03-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0025_user_applications_random_public_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='random_public_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
