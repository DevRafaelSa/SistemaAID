from django.contrib import admin
from .models import User
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm

# Register your models here.

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model: User

    list_display = ('id','first_name','username', 'email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('first_name', 'username', 'email')