from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from django.contrib import messages

from .models import CustomUser
# Create your views here.

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user'
    login_url = 'login_user'


    def get_object(self):
        return get_object_or_404(CustomUser, pk=self.request.user.pk)


def search_user(request):
    query = request.GET.get("car_number")
    user = None
    if query:
        try:
            user = CustomUser.objects.get(car_number=query)
        except CustomUser.DoesNotExist:
            user = None
    return render(request, "index.html", {"user": user})
    

class CustomRegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        car = request.POST.get("car_name")
        car_number = request.POST.get("car_number")
        car_color = request.POST.get("car_color")

        if password != confirm_password:
            messages.error(request, "Parollar mos kelmadi.")
            return render(request, "register.html")
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Bunday foydalanuvchi nomi allaqachon mavjud")
            return render(request, "register.html")
        
        if CustomUser.objects.filter(car_number=car_number).exists():
            messages.error(request, "Bunday avtomobil raqami allaqachon mavjud")
            return render(request, 'register.html')
        
        user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name,
                                              phone_number=phone_number, car=car, car_number=car_number, car_color=car_color)
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz")
            return redirect('search_user')


class CustomLoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Hisobga kirdingiz")
            return redirect('search_user')
        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol noto'g'ri")
            return render(request, 'login.html')
        
    
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Hisobdan chiqdingiz!")
        return redirect('login_user')
    

