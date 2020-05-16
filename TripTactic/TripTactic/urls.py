"""TripTactic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers

from cities.views import CityViewSet
from countries.views import CountryViewSet
from events.views import EventViewSet
from places.views import PlaceViewSet
from plans.views import PlanViewSet
from transportProviders.views import TransportProviderViewSet
from transports.views import TransportViewSet
from trips.views import TripViewSet
from users.views import UserViewSet
from usersFeedBacK.views import UserFeedBackViewSet

router = routers.DefaultRouter()

router.register(r'cities', CountryViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'events', EventViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'transportProviders', TransportProviderViewSet)
router.register(r'transports', TransportViewSet)
router.register(r'trips', TripViewSet)
router.register(r'users', UserViewSet)
router.register(r'userFeedBack', UserFeedBackViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/', include(router.urls)),
]
