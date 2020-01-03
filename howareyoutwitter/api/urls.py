from django.urls import path

from . import views

urlpatterns = [
    path('auth', views.AuthenticateView.as_view(), name='authenticate-view'),
]