from django.urls import path

from apps.views.authorization.views import SingInViewFunction, LoginInViewFunction


urlpatterns = [
    path('login-in/', LoginInViewFunction, name='login'),
    path('sing-in/', SingInViewFunction, name='sing'),
]
