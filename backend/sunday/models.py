

from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.postgres.fields import ArrayField

from django.conf import settings


class DirectorApps(models.Model):
    firstname = models.CharField(
        max_length=30, null=False, default='Did not enter a name')
    lastname = models.CharField(
        max_length=30, null=False, default='Did not enter a name')
    bio = models.TextField(
        max_length=300, null=False, default="Did Not enter a bio")
    projects = models.TextField(
        max_length=400, null=False, default="Did Not enter any projects")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default="")
    archived = models.TextField(max_length=30, default="null")


class Notifications(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, null=False, default=1)


class User(AbstractUser):
    pass


class StripeCustomer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default="")
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s' % (self.stripeCustomerId, self.stripeSubscriptionId)


class PersonalProjects(models.Model):
    description = models.TextField(default="3 Paragraphs, Feel free to brag!")
    title = models.CharField(max_length=50, default="none", null=False)
    role = models.CharField(max_length=50, default="none", null=False)
    poster = models.ImageField(
        upload_to='images/', default="///", max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, null=False, default=1)


class Actors(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default="")

    Hispanic_Latino = 'Hispanic/Latino'
    Asian_PacificIslander = 'Native Hawaiian/Pacific Islander'
    Asian = 'Asian'
    AfricanAmerican = 'Black/African American'
    NativeAmerican = 'Native American/Alaskan Native'
    MiddleEastern = 'Middle Eastern'
    not_provided = 'none'
    Ethnicity_choices = (
        (Hispanic_Latino, 'Hispanic/Latino'),
        (Asian_PacificIslander, 'Native Hawaiian/Pacific Islander'),
        (Asian, 'Asian'),
        (MiddleEastern, 'Middle Eastern'),
        (AfricanAmerican, 'Black/African American'),
        (NativeAmerican, 'Native American/Alaskan Native'),
    )

    ethnicity = models.CharField(max_length=50,
                                 choices=Ethnicity_choices,
                                 default=not_provided, null=True)

    bio = models.TextField(
        default="3 Paragraphs, Feel free to brag!", null=True)
    email = models.TextField(default="For Castings", null=True)
    crew_positions = models.CharField(
        max_length=50, default="NO VALUE", blank=True, null=True)

    age = models.IntegerField(blank=True, null=True)
    age_range = models.CharField(max_length=50, default="none", null=False)
    Directors = 'Directors'
    Actors = 'Actors'
    Crew = 'Crew'
    Dancers = 'Dancers'
    Writers = 'Writers'
    Photographers = 'Photographers'
    Postproduction = "Post Production"
    Production = "Production"
    Makeup = "Makeup Artist"
    Group_choices = (
        (Directors, 'Directors'),
        (Actors, 'Actors'),
        (Crew, 'Crew'),
        (Photographers, 'Photographers'),
        (Postproduction, 'Post Production'),
        (Production, 'Production'),
        (Makeup, 'Makeup Artist'),
        (Dancers, 'Dancers'),
        (Writers, 'Writers'),

    )

    group = models.CharField(
        max_length=50, choices=Group_choices, default="none", null=True)
    location = models.CharField(
        max_length=50, default="Where are you based?", null=True)
    middle = models.CharField(max_length=30, default="", null=True)
    firstname = models.CharField(max_length=25, default="")
    lastname = models.CharField(max_length=25, default="")

    resume = models.FileField(upload_to='uploads/',
                              null=True, default="no resume")
    headshot = models.ImageField(
        upload_to='images/', default="Please title: FIRSTNAME_LASTNAME", null=True)
    website = models.CharField(
        max_length=200, default="if applicable", null=True)

    Instagram_Handle_if_applicable = models.TextField(
        max_length=100, default="no handle", null=True)

    youtube_or_vimeo = models.TextField(
        max_length=300, default="no url", null=True)

    linkedIn = models.TextField(max_length=300, default="no url", null=True)

    project_types = models.TextField(
        max_length=200, default="no url", null=False)

    writing_genres = models.TextField(
        max_length=300, default="no url", null=True)

    education_background = models.TextField(
        max_length=150, default="no url", null=True)

    union = models.TextField(
        max_length=150, default="Missing Field", null=True)

    pronouns = models.TextField(
        max_length=150, default="no url", null=True)
    languages_spoken = models.TextField(
        max_length=1000, default="no url", null=True)

    def __str__(self):
        return self.firstname


class Photos(models.Model):
    photos = models.ImageField(upload_to='uploads/',
                               null=True, default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default="1", null=True)


class WritingSamples(models.Model):
    samples = models.FileField(upload_to='uploads/',
                               null=True, default="")
    thumbnail = models.ImageField(upload_to='uploads/',
                                  null=True, default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default="1", null=True)


class Reel(models.Model):
    reel = models.FileField(upload_to='uploads/',
                            null=True, default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default="1", null=True)
    thumbnail = models.ImageField(upload_to='uploads/',
                                  null=True, default="")


class MemberActors(models.Model):

    bio = models.TextField(default="3 Paragraphs, Feel free to brag!")
    firstname = models.CharField(max_length=25, default="")
    headshot = models.ImageField(
        upload_to='images/', default="Please title: FIRSTNAME_LASTNAME")
    Directors = 'Directors'
    Actors = 'Actors'
    Crew = 'Crew'
    Dancers = 'Dancers'
    Writers = 'Writers'
    Photographers = 'Photographers'
    Postproduction = "Post Production"
    Production = "Production"
    Makeup = "Makeup Artist"
    Group_choices = (
        (Directors, 'Directors'),
        (Actors, 'Actors'),
        (Crew, 'Crew'),
        (Photographers, 'Photographers'),
        (Postproduction, 'Post Production'),
        (Production, 'Production'),
        (Makeup, 'Makeup Artist'),
        (Dancers, 'Dancers'),
        (Writers, 'Writers'),

    )
    group = models.CharField(
        max_length=50, choices=Group_choices, default="none", null=True)

    def __str__(self):
        return self.firstname


class Directors(models.Model):
    animation = models.BooleanField(default=False)
    horror = models.BooleanField(default=False)
    short_film = models.BooleanField(default=False)
    # firstname = models.CharField(max_length=25,default="")
    # middle = models.CharField(max_length = 30,default="")
    # lastname = models.CharField(max_length=25,default="")
    # email = models.TextField(default="For Castings")
    # location = models.CharField(max_length=50, default="Where are you based?")
    # bio = models.TextField(default="3 Paragraphs, Feel free to brag!")
    # resume = models.FileField(upload_to='uploads/',null=True)
    # headshot = models.ImageField(upload_to='images/',default="Please title: FIRSTNAME_LASTNAME"
    # stillPhoto = models.ImageField(upload_to="images/",default='')
    # projects = models.BooleanField(default=False)
    # # looking = models.
    # # nameOfProject
    # logline = models.TextField(default='')
    # cast_info = models.TextField(default="")
    # Location_of_film = models.CharField(max_length=100, default='')
    # crew_position = models.CharField(max_length=255,default='')
    # stillPhoto = models.ImageField(upload_to="images/",default='')
    # # Date_of_filming = models.CharField(max_length=5,default='')
    # reel = models.CharField(max_length=200, default="")
    # website = models.CharField(max_length=200, default="if applicable")

    # Hispanic_Latino = 'Hispanic/Latino'
    # Asian_PacificIslander = 'Native Hawaiian/Pacific Islander'
    # Asian = 'Asian'
    # AfricanAmerican = 'Black/African American'
    # NativeAmerican = 'Native American/Alaskan Native'
    # MiddleEastern = 'Middle Eastern'
    # not_provided = 'none'

    # Ethnicity_choices = (
    #     (Hispanic_Latino, 'Hispanic/Latino'),
    #     (Asian_PacificIslander, 'Native Hawaiian/Pacific Islander'),
    #     (Asian, 'Asian'),
    #     (MiddleEastern, 'Middle Eastern'),
    #     (AfricanAmerican, 'Black/African American'),
    #     (NativeAmerican, 'Native American/Alaskan Native'),
    # )

    # ethnicity = models.CharField(max_length = 50,
    #     choices = Ethnicity_choices,
    #     default = not_provided)


class Listings(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default="1")
    title = models.TextField(max_length=300, default="")
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    state_location = models.CharField(max_length=50, default="")
    city_location = models.CharField(max_length=100, default="")
    overview = models.TextField(default="null")
    studio = models.CharField(max_length=40)
    poster = models.FileField(upload_to='images/', default="///", null=True)
    crew_positions = models.TextField(
        max_length=300, default="", null=True)
    post_production_positions = models.TextField(
        max_length=300, default="", null=True)
    # roles = models.ForeignKey(FilmRoles,
    #                           on_delete=models.PROTECT, null=True)

    genre = models.CharField(max_length=100,
                             default="null")
    director_email = models.CharField(max_length=255,
                                      default="null")
    director_name = models.CharField(max_length=255,
                                     default="null")

    Paid = "Paid"
    Volunteer = "Volunteer"
    Status_Choices = (
        (Paid, 'Paid'),
        (Volunteer, 'Volunteer'),
    )
    status = models.CharField(max_length=12,
                              choices=Status_Choices,
                              default="null")

    Fulltime = "Fulltime"
    Part_Time = "Part time"
    JOB_CHOICES = (
        (Fulltime, "Fulltime"),
        (Part_Time, 'Part time'),
    )
    job_type = models.CharField(max_length=15,
                                choices=JOB_CHOICES,
                                default="null")
    random_public_id = models.CharField(max_length=100, null=True)
    date_submitted = models.CharField(max_length=200, null=True)


class FilmRoles(models.Model):
    character_name = models.CharField(
        max_length=100, default="Did not enter a Name", null=True)
    role_name = models.CharField(
        max_length=100, default="Did not enter a Name", null=True)
    ethnicity = models.CharField(
        max_length=100, default="Did not enter a Name", null=True)

    listing = models.ForeignKey(Listings,
                                on_delete=models.PROTECT, null=True)
    role_thumbnail = models.TextField(
        default="", null=True)
    role_type = models.CharField(
        max_length=100, default="Did not enter a role type", null=True)
    role_description = models.TextField(
        max_length=3000, default="No Description Provided", null=True)
    role_status = models.CharField(
        max_length=100, default="Open", null=True)
    listing_public_id = models.CharField(
        max_length=200, default="Open", null=True)
    date_submitted = models.CharField(
        max_length=200, default="Open", null=True)


class Memberlistings(models.Model):

    title = models.TextField(max_length=300, default="")
    start_date = models.DateField(null=True)
    poster = models.FileField(upload_to='images/', default="///", null=True)
    overview = models.TextField(default="null")
    random_public_id = models.CharField(max_length=100, null=True)

    Animation = "Animation"
    Documentary = "Documentary"
    Experimental = "Experimental"
    Feature = "Feature"
    Music_Video = "Music Video"
    Short = "Short"
    Student = "Student"
    Television = "Television"
    Virtual_Reality = "Virtual Reality"
    Web_New_Media = "Web/New Media"
    Theater = "Theater"

    genre = models.CharField(max_length=100,

                             default="null")


class AcceptedRoles(models.Model):
    role_name = models.CharField(
        max_length=255, null=True)
    name = models.CharField(
        max_length=255, null=True)
    email = models.CharField(
        max_length=255, null=True)
    profile_picture = models.CharField(
        max_length=255, null=True)
    listing = models.ForeignKey(Listings,
                                on_delete=models.PROTECT, null=True)
    public_id_of_listing = models.CharField(
        max_length=255, null=True)


class DeclinedRoles(models.Model):
    role_name = models.CharField(
        max_length=255, null=True)
    name = models.CharField(
        max_length=255, null=True)
    email = models.CharField(
        max_length=255, null=True)
    profile_picture = models.CharField(
        max_length=255, null=True)
    listing = models.ForeignKey(Listings,
                                on_delete=models.PROTECT, null=True)
    public_id_of_listing = models.CharField(
        max_length=255, null=True)


class User_applications(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, default="1", null=True)
    name = models.CharField(
        max_length=80, default="Did not enter a Name", null=True)
    listing = models.ForeignKey(
        Listings,  on_delete=models.CASCADE, default="1", related_name="listing", null=True)
    role = models.CharField(
        max_length=60, default="Did not enter a Role", null=True)
    company = models.CharField(
        max_length=60, default="Did not enter a Company", null=True)
    title = models.CharField(max_length=60, default="No Title", null=True)
    archived = models.CharField(max_length=60, default="null", null=True)
    date_submitted = models.CharField(max_length=200, null=True)
    listing_url = models.CharField(max_length=255, null=True)
    listing_thumbnail = models.TextField(null=True)
    random_public_id_of_listing = models.CharField(max_length=100, null=True)
    random_public_id_of_applicant = models.CharField(max_length=100, null=True)
    profile_picture = models.CharField(max_length=255, null=True)
    Pending = "Pending"
    Accepted = "Accepted"
    Rejected = "Rejected"

    STATUS_CHOICES = (
        (Pending, "Pending"),
        (Accepted, "Accepted"),
        (Rejected, "Rejected"),
    )
    status = models.CharField(max_length=15,
                              null=True,
                              default="null")


class Thumbnails(models.Model):
    thumbnail = models.ImageField(
        upload_to='images/', default="///", max_length=300)
    category_name = models.CharField(max_length=255, null=True)
