# Generated by Django 3.0.6 on 2021-06-10 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0059_auto_20210610_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='crewCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('thumbnail', models.ImageField(default='', null=True, upload_to='uploads/')),
                ('card_title', models.TextField(default='')),
            ],
        ),
    ]
