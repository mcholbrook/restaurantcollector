from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant, Profile, User, Note
# Create your views here.

def home(request):
  return render(request, 'home.html')