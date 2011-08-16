from .models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.forms import ModelForm

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction

# Create your views here.
def new(req):
    if req.method == 'GET':
        form = TransactionForm()
        return render_to_response('new_transaction.html', {'form':form, 'total_left':Budget.default().amount_left})
    if req.method == 'POST':
        f = TransactionForm(req.POST)
        new_transaction = f.save(commit=False)

        print 'It is POST'
    return HttpResponse("New")

def home(req):
    return HttpResponse("View")
