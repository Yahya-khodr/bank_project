
from django.urls import path
from . import views


urlpatterns = [
    path('create_account',views.create_account),
    path('accounts',views.user_accounts),
    path('add_money',views.add_money)
]
