# Generated by Django 3.0.6 on 2021-04-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0032_user_applications_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_applications',
            name='profile_picture',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
