from django.contrib import admin
from .models import Expense, Payslip, Employee, Deposit, Withdrawal, Customer, Purchases,Sale,warehouse

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('Transaction_name', 'title', 'amount', 'category',)
    list_filter = ('Transaction_name', 'title', 'amount', 'category')
    search_fields = ('Transaction_name', 'title', 'amount', 'category')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'namefirst', 'namelast', 'age', 'country', 'email', 'sex', 'phone', 'password', 'state', 'postcode',
        'money',)


@admin.register(Payslip)
class PayslipAdmin(admin.ModelAdmin):
    list_display = ('Employee', 'date', 'basic_pay', 'benefits')


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'timestamp','purpose')


@admin.register(Withdrawal)
class WithdrawalsAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'timestamp','purpose')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_no', 'first_name', 'last_name', 'company_name')

@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'date', 'warehouse', 'supplier', 'status','date_of_purchase','Amount')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('invoice_number','date','warehouse','customer','remarks','requisition_number','Amount')

@admin.register(warehouse)
class warehouseAdmin(admin.ModelAdmin):
    list_display = ('name','Product','Quantity','supplier','Date_recieved')