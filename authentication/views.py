from django.shortcuts import render
import json
from django.contrib.auth import authenticate
# Create your views here.

def login(request):
    if  request.method== "POST":
        data =json.loads( request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username , password=password)
    else: 
        ...
