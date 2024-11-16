from django.shortcuts import render, redirect

from django.contrib import messages


# Create your views here.

#===========Transaction views========================
# def deposit(self, amount):
#         self.amount = amount
#         if self.amount > 0 :
#             self.balance = self.balance + self.amount
#             return f'You deposited the sum of {self.amount}. Your new balance is {self.balance}'
#         else:
#             return f'Your amount must be a positive number'

#     def withdraw(self, amount):
#         self.amount = amount
#         if self.amount < self.balance :
#             self.balance = self.balance - self.amount
#             return f'You withdrew {self.amount}. Your current balance is {self.balance}'
#         else:
#             return f"Insufficient Funds!"

#     def transfer(self, amount):
#         self.amount = amount
#         if self.amount < self.balance :
#             self.balance = self.balance - self.amount
#             return f'You transfered {self.amount}'
#     def check_balance(self):
#         return self.balance


