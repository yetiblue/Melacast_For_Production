# Generated by Django 3.0.6 on 2021-04-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0035_filmroles_role_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmroles',
            name='date_submitted',
            field=models.CharField(default='Open', max_length=200, null=True),
        ),
    ]
