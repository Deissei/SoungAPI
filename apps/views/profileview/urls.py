from django.urls import path

from apps.views.profileview.views import ProfileViewFunction


urlpatterns = [
    path('profile/', ProfileViewFunction, name='profile'),
]
