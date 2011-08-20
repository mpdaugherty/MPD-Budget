from django.db import models
from datetime import date
import calendar

#def Currency:
#    exchange_rate = models.FloatField()

# Create your models here.
class Budget(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total = models.DecimalField(decimal_places=2, max_digits = 16)
#    currency

    @property
    def amount_left(self):
        today = date.today()
        return reduce(lambda a, b: a-b.amount, self.transactions.filter(date__year=today.year, date__month=today.month), self.total)

    @classmethod
    def default(cls):
        '''This method should probably be temporary once we have multiple accounts, etc.  For
        now, it just returns the budget object that we use for Judy and Mike.'''
        return Budget.objects.get(pk=1)

    @property
    def ideal_amount_left(self):
        today = date.today()
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        days_left = days_in_month - today.day + 1
        return (days_left / days_in_month) * self.total

    @property
    def ideal_amount_per_day(self):
        today = date.today()
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        return self.total / days_in_month

    def __unicode__(self):
        return self.name

class Transaction(models.Model):
    budget = models.ForeignKey(Budget, related_name='transactions')
    date = models.DateField(default=date.today())
    amount = models.DecimalField(decimal_places=2, max_digits = 16)
    note = models.TextField()
    #    currency = models.ForeignKeyField(choices=['RMB','USD'])

    def __unicode__(self):
        return '{0} RMB - {1}'.format(self.amount, self.note)
