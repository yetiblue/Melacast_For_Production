# Generated by Django 3.0.6 on 2021-03-24 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0022_auto_20210324_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=255, null=True)),
                ('firstname', models.CharField(max_length=255, null=True)),
                ('lastname', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('profile_picture', models.CharField(max_length=255, null=True)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunday.Listings')),
            ],
        ),
    ]