# Generated by Django 3.0.6 on 2021-03-25 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0024_auto_20210324_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_applications',
            name='random_public_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]