from rest_framework import serializers


from .models import Actors, crewCards, WritingSamples, Reel, Listings, User_applications, Directors, User, DirectorApps, Notifications, Memberlistings, PersonalProjects, MemberActors, Photos, FilmRoles, StripeCustomer, AcceptedRoles, DeclinedRoles, Thumbnails


class UserSerializer(serializers.ModelSerializer):

    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        exclude = ["username", "password"]
        model = User


class ThumbnailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Thumbnails


class stripeCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = StripeCustomer


class AcceptedRolesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AcceptedRoles


class CrewCardsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = crewCards


class DeclinedRolesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DeclinedRoles


class FilmRolesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FilmRoles


class MemberlistingsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Memberlistings


class WritingSamplesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = WritingSamples


class ReelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Reel


class PhotosSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Photos


class MemberActorsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = MemberActors


class PersonalProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = PersonalProjects


class DirectorAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorApps
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = '__all__'


class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = '__all__'


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = '__all__'


class UserappsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_applications
        fields = '__all__'
