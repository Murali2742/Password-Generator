from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    thepassword=""
    character = list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))
    if(request.GET.get('UpperCase')):
        character.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if(request.GET.get('Specialcharacter')):
        character.extend('%?/.><@')
    if(request.GET.get('numbers')):
        character.extend('1234567890')



    for i in range(length):
        thepassword+=random.choice(character)
    pw=password
    return render(request,'generator/password.html', {'password':thepassword})

