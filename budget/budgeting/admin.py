from django.contrib import admin
from .models import Budget, Transaction

class BudgetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Budget, BudgetAdmin)

class TransactionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Transaction, TransactionAdmin)
