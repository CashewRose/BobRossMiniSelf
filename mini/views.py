from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from .models import Birthday

# Create your views here.

def index(request):
    return render(request, 'mini/index.html')

def birthday(request):
    birthday = Birthday.objects.all().values()
    birthday_list = list(birthday)
    return JsonResponse(birthday_list, safe=False)
