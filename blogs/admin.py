from django.contrib import admin
from .models import people


class Showblogs(admin.ModelAdmin):
    list_display = ["name","age","phone"]


# Register your models here.

admin.site.register(people,Showblogs)

