# Generated by Django 3.0.6 on 2021-03-25 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0026_listings_random_public_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_applications',
            old_name='random_public_id',
            new_name='random_public_id_of_applicant',
        ),
        migrations.AddField(
            model_name='user_applications',
            name='random_public_id_of_listing',
            field=models.CharField(max_length=100, null=True),
        ),
    ]