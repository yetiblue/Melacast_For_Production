# Generated by Django 3.0.6 on 2021-05-29 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0048_memberlistings_random_public_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberlistings',
            name='poster',
            field=models.FileField(default='///', null=True, upload_to='images/'),
        ),
    ]
