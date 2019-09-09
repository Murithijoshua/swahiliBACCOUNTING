"""treehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accountingApp.views import index,profitandloss, other_lib, liabilities_lib, payments, current_assets, \
     transactions

from accountingApp.views import home

from accountingApp.views import accounts_payable

urlpatterns = [

    path('admin/', admin.site.urls),
    path('index', index, name="index"),
    path('', home, name="home"),
    path('charts/',profitandloss, name="charts"),
    path('other_lib/', other_lib, name="other_lib"),
    path('liabilities_lib/', liabilities_lib, name="liabilities_lib"),
    path('pending_payments/', payments, name="pending_payments"),
    path('current_assets/', current_assets, name="current_assets"),
    path('fixed_assets/', accounts_payable, name="accounts_payable"),
    path('transactions/', transactions, name="transactions"),
]
