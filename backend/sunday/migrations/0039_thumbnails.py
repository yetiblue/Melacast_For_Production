# Generated by Django 3.0.6 on 2021-04-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0038_actors_languages_spoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(default='///', max_length=300, upload_to='images/')),
            ],
        ),
    ]