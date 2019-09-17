import django
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.db import models

# customers
from django.utils import timezone


class Customer(models.Model):
    customer_no = models.CharField(max_length=100)  # LLL-FFF-N
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True)
    is_company = models.BooleanField()
    PRICE_CHOICES = (
        ('R', 'Retail'),
        ('W', 'Wholesale'),
        ('D', 'Dealer'),
        ('S', 'Special'),
    )
    price_type = models.CharField(max_length=2, choices=PRICE_CHOICES, default='R')
    unit_number = models.CharField(max_length=50, blank=True, \
                                   verbose_name='House/Appt No')
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    vat_registration_number = models.IntegerField(default=0, blank=True)
    business_registration_number = models.CharField(max_length=9, blank=True)
    discount_percent = models.FloatField(default=0, blank=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('first_name', 'last_name'),)

    # stock in warehouse


class warehouse(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)
    Product = models.CharField(max_length=100, default='', unique=True)
    Quantity = models.IntegerField()
    supplier = models.CharField(max_length=100, default='', unique=True)
    Date_recieved = models.DateTimeField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    # stocks originality & description
    class Country(models.Model):
        name = models.CharField(max_length=100, unique=True)

        class Meta:
            ordering = ['name']
            verbose_name_plural = 'Countries'

        def __unicode__(self):
            return u'%s' % self.name


class Category(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)
    code = models.CharField(max_length=10, default='')
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return u'%s - %s' % (self.code, self.name)


class Colour(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Stock(models.Model):
    SQUARE_FEET = 'SF'
    SQUARE_METRE = 'SM'
    UNIT = 'U'
    UNIT_CHOICES = (
        (SQUARE_FEET, 'Square Feet'),
        (SQUARE_METRE, 'Square Metre'),
        (UNIT, 'Unit'),
    )

    item_code = models.CharField(max_length=50, unique=True)
    item_name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, default='')
    # colour = models.ForeignKey(Colour, null=True, blank=True)
    size = models.CharField(max_length=50, blank=True)
    tonality = models.CharField(max_length=5, blank=True)
    caliber = models.CharField(max_length=5, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, )
    retail_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    retail_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=UNIT)
    wholesale_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    wholesale_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=UNIT)
    dealer_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    dealer_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=UNIT)
    special_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    special_unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=UNIT)
    pieces_per_box = models.IntegerField(null=True, blank=True, default=0)
    exempt_flag = models.BooleanField(default=False)
    nonstock_flag = models.BooleanField(default=False)
    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s - %s' % (self.item_code, self.description)

    def info(self):
        if self.country:
            country_name = self.country.name
        else:
            country_name = ''

        return {
            'item_code': self.item_code,
            'description': self.description,
            'category': self.category.name,
            'retail_price': '%.2f' % self.retail_price,
            'retail_unit': self.retail_unit,
            'wholesale_price': '%.2f' % self.wholesale_price,
            'wholesale_unit': self.wholesale_unit,
            'dealer_price': '%.2f' % self.dealer_price,
            'dealer_unit': self.dealer_unit,
            'special_price': '%.2f' % self.special_price,
            'special_unit': self.special_unit,
            'pieces_per_box': self.pieces_per_box,
            'exempt_flag': self.exempt_flag,
            'nonstock_flag': self.nonstock_flag,
            'country': country_name,
        }

    def customer_price(self, price_type):
        if price_type == 'R':
            return self.retail_price
        elif price_type == 'W':
            return self.wholesale_price
        elif price_type == 'D':
            return self.dealer_price
        else:
            return self.special_price


# sales
class Sale(models.Model):
    invoice_number = models.IntegerField()  # CHN starts at N=1
    date = models.DateField()
    # sales_agent = models.ForeignKey('staffs.SalesAgent', blank=True, null=True, on_delete=models.CASCADE)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    remarks = models.CharField(max_length=255, blank=True)
    requisition_number = models.CharField(max_length=255, blank=True)
    # cart = models.ForeignKey('stock_carts.StockCart', blank=True, null=True, on_delete=models.CASCADE)
    # contact_list = models.ForeignKey('contacts.ContactList', blank=True, null=True, on_delete=models.CASCADE)
    sold_on=models.DateTimeField(auto_now_add=True)
    Amount = models.IntegerField()

    # purchases

class Purchases(models.Model):
    invoice_no = models.IntegerField()  # CHN starts at N=1
    date= models.DateTimeField(auto_now_add=True)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    supplier = models.CharField(max_length=233)
    status = models.CharField(max_length=255, blank=True)
    date_of_purchase =  models.DateTimeField(auto_now_add=True)
    Amount = models.IntegerField()

    # expense initialization


class Expense(models.Model):
    choice = (
        ('bills', 'Bills'),
        ('Payments', 'payments'),
        ('pettycash', 'Pettycash'),
        ('other', 'Other'),
    )

    Transaction_name = models.CharField(max_length=250, )
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=250, choices=choice)


class Meta:
    ordering = ('-amount',)

    # payrolls


class Employee(AbstractBaseUser):
    namefirst = models.CharField("first name".capitalize(), max_length=16)
    namelast = models.CharField("last name".capitalize(), max_length=16)

    age = models.IntegerField()
    country = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    state = models.CharField(max_length=250)
    money = models.IntegerField()
    postcode = models.CharField(max_length=250)
    date_of_birth = models.DateField("Date of Birth", default=None)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
        a = self.namefirst
        b = self.namelast
        full_name = f'{a.capitalize()} {b.capitalize()}'
        return full_name


class Payslip(models.Model):
    Employee = models.ForeignKey(Employee, related_name='payroll', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, )
    basic_pay = models.IntegerField(default=0, name='basic_pay')
    benefits = models.IntegerField(default=0, name='benefits')

    # transactions model


class Deposit(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(
        User,
        related_name='deposits',
        on_delete=models.CASCADE,
    )
    purpose = models.CharField(max_length=240)
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('10.00'))
        ]
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Withdrawal(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(
        User,
        related_name='withdrawals',
        on_delete=models.CASCADE,
    )
    purpose = models.CharField(max_length=240)
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('10.00'))
        ]
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Interest(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(
        User,
        related_name='interests',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
