from django.contrib import admin
from .models import Budget, Transaction, UserBudget

class UserBudgetAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserBudget, UserBudgetAdmin)

class BudgetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Budget, BudgetAdmin)

class TransactionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Transaction, TransactionAdmin)
