from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    model = User
    list_display = ['email', 'is_doctor']
    list_filter = ('is_doctor',)
    search_fields = ('email',)