from .models import *
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.forms import ModelForm, TextInput

def upgrade_fields(f, widget=None, **kwargs):
    '''
    Upgrades fields to HTML5 where possible; includes jQuery date pickers for date fields, etc.
    '''

    formfield = f.formfield()

    if widget != None:
        # In this case, the user has specified the widget explicitly.
        formfield.widget = widget

    if isinstance(f, models.DateField):
        formfield.widget.format = '%m/%d/%Y'
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
        formfield.widget.input_type = 'date'
    if isinstance(f, models.DecimalField) or isinstance(f, models.IntegerField) or isinstance(f, models.FloatField):
        formfield.widget.input_type = 'number'
    if isinstance(f, models.EmailField):
        formfield.widget.input_type = 'email'
    if isinstance(f, models.DateTimeField):
        formfield.widget.input_type = 'datetime'
    if isinstance(f, models.TimeField):
        formfield.widget.input_type = 'time'
    return formfield

class TransactionForm(ModelForm):
    formfield_callback = upgrade_fields
    class Meta:
        model = Transaction
        exclude = { 'budget' }
        widgets = { 'note': TextInput(attrs={'size':30}) }

# Create your views here.
def home(req):
    if req.method == 'GET':
        form = TransactionForm()
        b = Budget.default()
        today = date.today()
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        days_left = days_in_month - today.day + 1
        return render_to_response('new_transaction.html',
                                  RequestContext(req,
                                                 {'form':form,
                                                  'total_left': b.amount_left,
                                                  'ideal_amount_per_day': b.ideal_amount_per_day,
                                                  'days_left': days_left,}))
    if req.method == 'POST':
        new_transaction = Transaction(budget = Budget.objects.get(id=1))
        f = TransactionForm(req.POST, instance=new_transaction)
        f.save()
        return redirect('home')
    return HttpResponse("What request method are you using?  It's unhandled...")

def view_transactions(req):
    budget = Budget.default()
    days = {}
    for t in budget.transactions.all():
        date = t.date
        try:
            day_model = days[date]
        except:
            day_model = {}
            days[date] = day_model
            day_model['amount_left'] = budget.amount_left_on_date(date)

        try:
            day_transactions = day_model['transactions']
        except:
            day_transactions = []
            day_model['transactions'] = day_transactions

        day_transactions.append(t)
    print days
    return render_to_response('history.html',
                              RequestContext(req,
                                             {'days': days}))
