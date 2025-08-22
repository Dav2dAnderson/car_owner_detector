from django.urls import path

from .views import search_user


urlpatterns = [
    path('search', search_user, name='search_user')
]


