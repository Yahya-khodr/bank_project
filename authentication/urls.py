from django.urls import path
from . import views



urlpatterns = [
    path('login',views.login),
    path('test_auth',views.test_auth)
]
