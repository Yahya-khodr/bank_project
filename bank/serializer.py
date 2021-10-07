

from bank.models import BankAccount


def account_serializer(bank_account : "BankAccount") -> dict:
    return {
        "bank_account" : str(bank_account.bank_account),
        "balance" : bank_account.balance
    }