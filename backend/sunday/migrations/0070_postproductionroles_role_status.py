# Generated by Django 3.0.6 on 2021-06-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0069_productionroles_role_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='postproductionroles',
            name='role_status',
            field=models.CharField(default='Open', max_length=10, null=True),
        ),
    ]
