# Generated by Django 3.0.6 on 2020-12-17 15:27

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animation', models.BooleanField(default=False)),
                ('horror', models.BooleanField(default=False)),
                ('short_film', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=300)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('location', models.CharField(default='', max_length=50)),
                ('overview', models.TextField(default='null')),
                ('studio', models.CharField(max_length=40)),
                ('poster', models.ImageField(default='///', upload_to='images/')),
                ('open_positions', models.TextField(default='', max_length=300)),
                ('genre', models.CharField(choices=[('Animation', 'Animation'), ('Documentary', 'Documentary'), ('Experimental', 'Experimental'), ('Feature', 'Feature'), ('Music Video', 'Music Video'), ('Short', 'Short'), ('Student', 'Student'), ('Television', 'Television'), ('Virtual Reality', 'Virtual Reality'), ('Web/New Media', 'Web/New Media'), ('Theater', 'Theater')], default='null', max_length=40)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Volunteer', 'Volunteer')], default='null', max_length=12)),
                ('job_type', models.CharField(choices=[('Fulltime', 'Fulltime'), ('Part time', 'Part time')], default='null', max_length=15)),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberActors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='3 Paragraphs, Feel free to brag!')),
                ('firstname', models.CharField(default='', max_length=25)),
                ('headshot', models.ImageField(default='Please title: FIRSTNAME_LASTNAME', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Memberlistings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=300)),
                ('start_date', models.DateField(null=True)),
                ('poster', models.ImageField(default='///', upload_to='images/')),
                ('overview', models.TextField(default='null')),
                ('genre', models.CharField(choices=[('Horror', 'Horror'), ('Action', 'Action'), ('Short Film', 'Short Film'), ('Romance', 'Romance'), ('Thriller', ' Thriller'), ('Drama', 'Drama'), ('Musical', ' Musical')], default='null', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User_applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Did not enter a Name', max_length=80, null=True)),
                ('role', models.CharField(default='Did not enter a Role', max_length=60, null=True)),
                ('company', models.CharField(default='Did not enter a Company', max_length=60, null=True)),
                ('title', models.CharField(default='No Title', max_length=60, null=True)),
                ('archived', models.CharField(default='null', max_length=60, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='null', max_length=15)),
                ('listing', models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='sunday.Listings')),
                ('user', models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(default='', null=True, upload_to='uploads/')),
                ('user', models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='3 Paragraphs, Feel free to brag!')),
                ('title', models.CharField(default='none', max_length=50)),
                ('role', models.CharField(default='none', max_length=50)),
                ('poster', models.ImageField(default='///', max_length=300, upload_to='images/')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DirectorApps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='Did not enter a name', max_length=30)),
                ('lastname', models.CharField(default='Did not enter a name', max_length=30)),
                ('bio', models.TextField(default='Did Not enter a bio', max_length=300)),
                ('projects', models.TextField(default='Did Not enter any projects', max_length=400)),
                ('archived', models.TextField(default='null', max_length=30)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethnicity', models.CharField(choices=[('Hispanic/Latino', 'Hispanic/Latino'), ('Native Hawaiian/Pacific Islander', 'Native Hawaiian/Pacific Islander'), ('Asian', 'Asian'), ('Middle Eastern', 'Middle Eastern'), ('Black/African American', 'Black/African American'), ('Native American/Alaskan Native', 'Native American/Alaskan Native')], default='none', max_length=50, null=True)),
                ('bio', models.TextField(default='3 Paragraphs, Feel free to brag!', null=True)),
                ('email', models.TextField(default='For Castings', null=True)),
                ('crew_positions', models.TextField(default='My Crew Positions', null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('age_range', models.CharField(default='none', max_length=50)),
                ('group', models.CharField(choices=[('Directors', 'Directors'), ('Actors', 'Actors'), ('Crew', 'Crew'), ('Photographers', 'Photographers'), ('Post Production', 'Post Production'), ('Production', 'Production'), ('Makeup Artist', 'Makeup Artist'), ('Dancers', 'Dancers'), ('Writers', 'Writers')], default='none', max_length=50, null=True)),
                ('location', models.CharField(default='Where are you based?', max_length=50, null=True)),
                ('middle', models.CharField(default='', max_length=30, null=True)),
                ('firstname', models.CharField(default='', max_length=25)),
                ('lastname', models.CharField(default='', max_length=25)),
                ('resume', models.FileField(default='no resume', null=True, upload_to='uploads/')),
                ('headshot', models.ImageField(default='Please title: FIRSTNAME_LASTNAME', null=True, upload_to='images/')),
                ('website', models.CharField(default='if applicable', max_length=200, null=True)),
                ('Reel_Link', models.FileField(default='no Reel', null=True, upload_to='uploads/')),
                ('Instagram_Handle_if_applicable', models.TextField(default='no handle', max_length=100, null=True)),
                ('Writing_Samples', models.FileField(default='no samples', null=True, upload_to='uploads/')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
