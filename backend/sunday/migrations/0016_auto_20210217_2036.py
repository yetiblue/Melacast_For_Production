# Generated by Django 3.0.6 on 2021-02-17 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0015_auto_20210216_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='roles',
        ),
        migrations.AddField(
            model_name='filmroles',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunday.Listings'),
        ),
    ]