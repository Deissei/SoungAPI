from django.urls import path

from apps.views.homepage.views import HomePageViewFunction


urlpatterns = [
    path('', HomePageViewFunction, name='homepage'),
]
