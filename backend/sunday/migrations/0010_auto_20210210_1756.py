# Generated by Django 3.0.6 on 2021-02-10 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sunday', '0009_auto_20210206_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(default='Did not enter a Name', max_length=100, null=True)),
                ('ethnicity', models.CharField(default='Did not enter a Name', max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='listings',
            old_name='open_positions',
            new_name='open_crew_positions',
        ),
        migrations.AddField(
            model_name='listings',
            name='roles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunday.FilmRoles'),
        ),
    ]
