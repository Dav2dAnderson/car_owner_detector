from django.shortcuts import render
from django.views import View

from .models import CustomUser
# Create your views here.




def search_user(request):
    query = request.GET.get("car_number")
    user = None
    if query:
        try:
            user = CustomUser.objects.get(car_number=query)
        except CustomUser.DoesNotExist:
            user = None
    return render(request, "index.html", {"user": user})
    


    
    
