from django.urls import path

from .views import search_user, CustomRegisterView, CustomLoginView, CustomLogoutView, ProfileView


urlpatterns = [
    path('search/', search_user, name='search_user'),
    path('register/', CustomRegisterView.as_view(), name="register_user"),
    path('login/', CustomLoginView.as_view(), name='login_user'),
    path('logout/', CustomLogoutView.as_view(), name='logout_user'),
    path('profile/', ProfileView.as_view(), name="profile" ),

]



