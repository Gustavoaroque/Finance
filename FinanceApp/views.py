from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    total_amount_expenses = 0
    total_amount_incomes = 0
    Expenses = Transaction.objects.filter(transaction_type='Expense')
    Incomes = Transaction.objects.filter(transaction_type='Income')
    print(Expenses)
    print('=====================')
    print(Incomes)

    for Ex in Expenses:
        total_amount_expenses = Ex.transaction_amount + total_amount_expenses
    for In in Incomes:
        total_amount_incomes = In.transaction_amount + total_amount_incomes
    context = {
        'title':'Home Page',
        'expenses_total':total_amount_expenses,
        'incomes_total':total_amount_incomes,
    }
    return render(request, 'HomePage.html', context)
