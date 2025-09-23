from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# Register your models here.
class ProfileAdmin(UserAdmin):
    model = Profile
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')

admin.site.register(Profile, ProfileAdmin)
