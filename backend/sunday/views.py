
import requests
import stripe
from sunday.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


from .models import Actors, WritingSamples, crewCards, Reel, Listings, User_applications, Directors, User, DirectorApps, Memberlistings, Notifications, PersonalProjects, MemberActors, Photos, FilmRoles, StripeCustomer, AcceptedRoles, DeclinedRoles, Thumbnails
from rest_framework import viewsets
from django.views import View
from django.http.response import JsonResponse, HttpResponse  # updated
from django.conf import settings

from url_filter.integrations.drf import DjangoFilterBackend
from .serializers import ActorSerializer, CrewCardsSerializer, WritingSamplesSerializer, ReelSerializer, ListingsSerializer, UserappsSerializer, DirectorSerializer, UserSerializer, DirectorAppsSerializer, NotificationsSerializer, MemberlistingsSerializer, MemberActorsSerializer, PersonalProjectsSerializer, PhotosSerializer, FilmRolesSerializer, stripeCustomerSerializer, AcceptedRolesSerializer, DeclinedRolesSerializer, ThumbnailsSerializer


# def add_new_customer(request):
#     client_id = 1
#     user = User.objects.get(id=client_id)
#     StripeCustomer.objects.create(
#         user=user,
#         stripeCustomerId="1",
#         stripeSubscriptionId="2"
#     )
#     print(user.groups.all())

#     return HttpResponse(status=200)
#     return(user.groups.all())

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        client_reference_id = session.get('client_reference_id')

        stripe_customer_id = session.get('subscription')
        stripe_subscription_id = session.get('subscription')

        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
        print('just subscribed')

        stripe_customer = StripeCustomer.objects.get(user=user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(
            stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)
        print(product.name)

        Actors.objects.filter(user=user).update(group=product.name)
        Actors.objects.filter(user=user).update(paid_listing=True)

        # print(product.objects.all())
    return HttpResponse(status=200)


@csrf_exempt
def paid_listing_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        client_reference_id = session.get('client_reference_id')

        user = User.objects.get(id=client_reference_id)
        print(user, "user")

        Actors.objects.filter(user=user).update(paid_listing=True)

        # print(product.objects.all())
    return HttpResponse(status=200)


class ThumbnailsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = Thumbnails
    queryset = Thumbnails.objects.all()
    serializer_class = ThumbnailsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class CrewCardsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = crewCards
    queryset = crewCards.objects.all()
    serializer_class = CrewCardsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class DeclinedRolesViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = DeclinedRoles
    queryset = DeclinedRoles.objects.all()
    serializer_class = DeclinedRolesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class AcceptedRolesViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = AcceptedRoles
    queryset = AcceptedRoles.objects.all()
    serializer_class = AcceptedRolesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class customerViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = StripeCustomer
    queryset = StripeCustomer.objects.all()
    serializer_class = stripeCustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class FilmRolesViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = FilmRoles
    queryset = FilmRoles.objects.all()
    serializer_class = FilmRolesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class DirectorAppViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = DirectorApps
    queryset = DirectorApps.objects.all()
    serializer_class = DirectorAppsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class WritingSamplesViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = WritingSamples
    queryset = WritingSamples.objects.all()
    serializer_class = WritingSamplesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class ReelViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = Reel
    queryset = Reel.objects.all()
    serializer_class = ReelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class PhotosViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = Photos
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class MemberlistingsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = Memberlistings
    queryset = Memberlistings.objects.all()
    serializer_class = MemberlistingsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class MemberActorsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = MemberActors
    queryset = MemberActors.objects.all()
    serializer_class = MemberActorsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class PersonalProjectsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = PersonalProjects
    queryset = PersonalProjects.objects.all()
    serializer_class = PersonalProjectsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NotificationsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = Notifications
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user', 'id']


class ActorViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    model = Actors
    queryset = Actors.objects.all()

    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class ListingsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset = Listings.objects.all().order_by('location')
    serializer_class = ListingsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class UserappsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset = User_applications.objects.all().order_by('status')
    serializer_class = UserappsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'


class DirectorsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset = Directors.objects.all()
    serializer_class = DirectorSerializer
