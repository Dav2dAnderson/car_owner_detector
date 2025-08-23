from django.urls import path

from .views import search_user, CustomRegisterView, CustomLoginView


urlpatterns = [
    path('search/', search_user, name='search_user'),
    path('register/', CustomRegisterView.as_view(), name="register_user"),
    path('login/', CustomLoginView.as_view(), name='login_user')
]



