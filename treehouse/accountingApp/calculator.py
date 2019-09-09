# # afrom .models import sale,Expense,Purchases
# # profit and loss
# class Profitandloss():
#     sales_amount = None
#     expenses_amount = None

#     @property
#     def netprofit(self):
#         return self.sales_amount - self.expenses_amount


# class Balanceshet(object):
#     sales_amount = None
#     current_assets = None
#     expenses_amount = None
#     purchases_amount = None
#     inventory = None
#     bankbalances = None
#     sales_amount = sale.objects.aggregate(sum('amount'))
#     purchases_amount=Purchases.objects.aggrgate(sum('amount'))
#     inventory=Wa
#     @property
#     def creditside(self):

#         p = self.sales_amount + self.current_assets + self.inventory
#         return p

#     @property
#     def debit(self):
#         y = self.bankbalances + self.purchases_amount + self.expenses_amount
#         return y

#     @property
#     def balanceshet_report(self):
#         balance_carried_forward = p - y
