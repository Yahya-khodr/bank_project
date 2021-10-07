
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from authentication.models import UserToken
import json
import uuid

from authentication.utils import is_authenticated
# Create your views here.


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        print(f"username:{username}, password:{password}")
        user = authenticate(
            request, username=username , password=password)
        if user is not None :
            
            user_token = UserToken.objects.create(user=user,token=uuid.uuid4())
            return JsonResponse({"token":str(user_token.token)})
        else:
            return JsonResponse({"message": "wrong credentials"})    
        


        
             


def test_auth(request):
    if  not is_authenticated(request):
        return JsonResponse({"message": "You are not authenticated"})
    return JsonResponse({"message": "You are authenticated"})