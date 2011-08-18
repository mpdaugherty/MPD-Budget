from .models import *
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.forms import ModelForm

# use jQuery date picker (from here: http://strattonbrazil.blogspot.com/2011/03/using-jquery-uis-date-picker-on-all.html)
def make_pretty_datefield(f):
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%m/%d/%Y'
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield

class TransactionForm(ModelForm):
    formfield_callback = make_pretty_datefield
    class Meta:
        model = Transaction
        exclude = { 'budget' }

# Create your views here.
def home(req):
    if req.method == 'GET':
        form = TransactionForm()
        return render_to_response('new_transaction.html', RequestContext(req, {'form':form, 'total_left':Budget.default().amount_left}))
    if req.method == 'POST':
        new_transaction = Transaction(budget = Budget.objects.get(id=1))
        f = TransactionForm(req.POST, instance=new_transaction)
        f.save()
        return redirect('home')
    return HttpResponse("What request method are you using?  It's unhandled...")
