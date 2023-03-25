from enum import Enum


class AccountType(Enum):
    CHECKING = 0
    SAVINGS = 1


class OverdraftException(Exception):
    pass


class BankAccount:

    def __init__(self, balance=0, accountType=AccountType.CHECKING):
        self.__accountType = accountType
        if balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0

    def getBalance(self):
        return self.__balance

    def getAccountType(self):  #Cannot change account type
        return self.__accountType


#will have a deposit and withdraw methods instead to change balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
        if amount > self.__balance:
            raise OverdraftException("Insufficient balance")
