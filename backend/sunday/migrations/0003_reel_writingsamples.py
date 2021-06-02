# Generated by Django 3.0.6 on 2020-12-27 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0002_memberactors_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='WritingSamples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('samples', models.FileField(default='', null=True, upload_to='uploads/')),
                ('user', models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reels', models.FileField(default='', null=True, upload_to='uploads/')),
                ('user', models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]