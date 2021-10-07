import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import bank
from bank.models import BankAccount
from django.http.response import JsonResponse
from authentication.utils import is_authenticated
from bank.serializer import account_serializer

# Create your views here.



@csrf_exempt
def create_account(request):
    if not is_authenticated(request):
        return JsonResponse(
            {"message":"you should be authenticated to create an account"})
    if request.method == "POST":
        bank_account =BankAccount.objects.create(user=request.user)
        return JsonResponse({"Message":"Success","bank_account":str(bank_account.bank_account)})


def user_accounts(request):
    if not is_authenticated(request):
        return JsonResponse(
            {"message":"you should be authenticated to see your accounts"})

    
    bank_accounts = BankAccount.objects.filter(user=request.user)
    return JsonResponse(
        {"user_accounts":account_serializer(bank_account)
        for bank_account in bank_accounts})

    # bank_accounts_list = []
    # for bank_account in bank_accounts:
    #     bank_accounts_list.append(serialize_bank_account(bank_account))
    # return JsonResponse({"accounts": bank_accounts_list})
@csrf_exempt
def add_money(request):
    if not is_authenticated(request):
        return JsonResponse(
            {"message":"you should be authenticated to see your accounts"})

    if request.method == "POST":
        
        account_data = json.loads(request.body)
        balance = account_data.get("balance")
        bank_account = BankAccount.objects.get(user=request.user)
        bank_token = bank_account.bank_account
        user = request.user
        if user is not None:
            user_balance = BankAccount.objects.create(
                user=request.user,bank_account= str(bank_token),balance=balance)
            return JsonResponse(
                {"Message":"Added Money to your balance",
                "Current_balance":user_balance.balance})
        else: JsonResponse({"Messsage":"Failed To Add Money To Your Account "})
