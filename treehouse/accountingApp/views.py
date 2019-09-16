from django.shortcuts import render
from django.db.models import Sum
from .models import Expense, Employee, Payslip, Withdrawal, Deposit, warehouse, Sale
from .models import Purchases
# from .calculator import Balanceshet


# from accountingApp. models import Stock


# from django.http import Httpresponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


# current assets carried forward

# current status from all inventories
def current_assets(request):
    pending = Sale.objects.all()
    # bank Balanceshet
    deposits = Deposit.objects.aggregate(Sum('amount'))
    sithdrawal= Withdrawal.objects.aggregate(Sum('amount'))
    amoun_deposits=deposits['amount__sum']
    amount=sithdrawal['amount__sum']
    bankbalance= abs(amoun_deposits - amount) 


    context = {
       'totals': pending,
        'balance': bankbalance
    }
    return render(request, 'current_asset.html', context)


# these are goods that are purchased on debit and company owes the suppliers
def accounts_payable(request):
    expense = warehouse.objects.all()
    context = {
        'expenses': expense
        # 'total_assets': y
    }
    return render(request, 'fixed_assets.html', context)


# bills


def liabilities_lib(request):
    expense = Expense.objects.all()
    context = {
        'expenses': expense
    }
    return render(request, 'liabilities_bills.html', context)


def payments(request):
    total = Employee.objects.aggregate(Sum('money'))
    Total_benefits = Payslip.objects.aggregate(Sum('benefits'))
    t = total['money__sum']
    Y = Total_benefits['benefits__sum']
    context = {
        'salaries': t,
        'promotions': Y

    }
    return render(request, 'pending_payments.html', context)


def other_lib(request):
    return render(request, 'other_lib')


def profitandloss(request):
    sales_amount = None
    expenses_amount = None
    purchases_amount=None
    sales=Sale.objects.aggregate(Sum('Amount'))
    purchases=Purchases.objects.aggregate(Sum('Amount'))
    expenses=Expense.objects.aggregate(Sum('amount'))
    """ getting the values from the dictonary and returning them as a numbers/decimals for computations purposes

    """
    sales_amount=sales['Amount__sum']
    purchases_amount = purchases['Amount__sum']
    expenses_amount = expenses['amount__sum']
    # if sales_amount< purchases_amount:
    loss=abs(sales_amount - (expenses_amount+ purchases_amount))
        # return loss
    # elif purchases_amount < sales_amount:
    profit=sales_amount - (expenses_amount+ purchases_amount)
        #   return profit
    context = {
    'profit':profit,
    'loss': loss
    }

    return render(request, 'chart.html', context)


def transactions(request):
    transaction_list = Deposit.objects.all()
    Deposits_list = Withdrawal.objects.all()
    context = {
        'transactions': transaction_list,
        'deposits': Deposits_list
    }
    return render(request, 'transactions.html', context)
