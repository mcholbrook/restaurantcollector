from django.contrib import admin
from .models import Restaurant, User, Profile, Note


# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Profile)
admin.site.register(Note)