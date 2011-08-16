from django.db import models

#def Currency:
#    exchange_rate = models.FloatField()

# Create your models here.
class Budget(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total = models.DecimalField(decimal_places=2, max_digits = 16)
#    currency

    @property
    def amount_left(self):
        return reduce(lambda a, b: a-b.amount, self.transactions.all(), self.total)

    @classmethod
    def default(cls):
        '''This method should probably be temporary once we have multiple accounts, etc.  For
        now, it just returns the budget object that we use for Judy and Mike.'''
        return Budget.objects.get(pk=1)

    OK = 1
    WARNING = 2
    NOT_ENOUGH_MONEY = 3
    def test_transaction(self, amount):
        predicted_amount_left = self.amount_left - amount
        if predicted_amount_left > 3000:
            return Budget.OK

        if predicted_amount_left < 0:
            return Budget.NOT_ENOUGH_MONEY

        return Budget.WARNING

class Transaction(models.Model):
    budget = models.ForeignKey(Budget, related_name='transactions')
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits = 16)
    note = models.TextField()
    #    currency = models.ForeignKeyField(choices=['RMB','USD'])
