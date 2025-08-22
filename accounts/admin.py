from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display=("username", "email", "phone_number", "car", "car_number", "car_color", "is_staff" )
    search_fields = ("username", "email", "phone_number", "car_number")
    ordering = ("username", )


    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields" : ("phone_number" , "car", "car_number", "car_color")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields" : ("phone_number", "car", "car_number", "car_color")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
