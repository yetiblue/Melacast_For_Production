# Generated by Django 3.0.6 on 2021-05-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0046_auto_20210428_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='poster',
            field=models.FileField(default='///', null=True, upload_to='images/'),
        ),
    ]
