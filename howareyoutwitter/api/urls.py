from django.urls import path

from . import views

urlpatterns = [
    path('auth', views.AuthenticateView.as_view(), name='authenticate-view'),
    path('search', views.SearchTweetsView.as_view(), name='search-tweets-view')
]