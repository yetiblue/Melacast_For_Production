# Generated by Django 3.0.6 on 2021-02-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0016_auto_20210217_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmroles',
            name='role_description',
            field=models.TextField(default='No Description Provided', max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='actors',
            name='crew_positions',
            field=models.CharField(blank=True, default='NO VALUE', max_length=50, null=True),
        ),
    ]
