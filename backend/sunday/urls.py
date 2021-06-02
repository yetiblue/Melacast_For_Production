from django.urls import include, path
from rest_framework import routers
from .import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
# router.register('heroes', views.HeroViewSet)
router.register('listings', views.ListingsViewSet)
router.register('actors', views.ActorViewSet)
router.register('apps', views.UserappsViewSet)
router.register('directors', views.DirectorsViewSet)
router.register('users', views.UserViewSet)
router.register('directorapps', views.DirectorAppViewSet)
router.register('notifications', views.NotificationsViewSet)
router.register('memberlistings', views.MemberlistingsViewSet)
router.register('memberactors', views.MemberActorsViewSet)
router.register('personalprojects', views.PersonalProjectsViewSet)
router.register('photos', views.PhotosViewSet)
router.register('filmroles', views.FilmRolesViewSet)
router.register('writingsamples', views.WritingSamplesViewSet)
router.register('reels', views.ReelViewSet)
router.register('customers', views.customerViewSet)
router.register('acceptedroles', views.AcceptedRolesViewSet)
router.register('declinedroles', views.DeclinedRolesViewSet)
router.register('thumbnails', views.ThumbnailsViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    # path('newcustomer/', views.add_new_customer),
    # path('products/', views.products),
    path('webhook/', views.stripe_webhook),

    # path('auth/users/',include('')

    # path('templates/new/', views.template_new, name='template_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
