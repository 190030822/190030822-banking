from django.shortcuts import render
from customers.models import Customer
from customers.forms import MoneyTransferForm
from django.forms import forms
from django.contrib import messages
from customers.models import Hist
# Create your views here.

def home(request):
    return render(request,"customers/home.html")

def view_cust(request):
    custs = Customer.objects.all()
    return render(request,"customers/details.html",{'customers' : custs})


def transfer(request):
    if request.method == "POST":
        form = MoneyTransferForm(request.POST)
        if (form.is_valid()):
            try:
                user = Customer.objects.get(email=request.POST.get('From'))
                user.curr_bal -= int(request.POST.get('amount'))
                
            except Customer.DoesNotExist:
                user = None
            try:
                userr = Customer.objects.get(email = request.POST.get('To')) 
                userr.curr_bal +=int( request.POST.get('amount'))
                
            except Customer.DoesNotExist:
                userr = None
            if  user == None:
                messages.error(request, "give proper sender email")
                form = MoneyTransferForm()
                context = {'form': form}
                return render(request, "customers/transaction.html", context)
            if int(request.POST.get('amount')) > user.curr_bal:
                messages.error(request,'your transfer amount need to be less than your balance')
                form = forms.MoneyTransferForm()
                context = {'form': form}
                return render(request,"customers/transaction.html",context)
            if int(request.POST.get('amount'))  < 0:
                messages.error(request,"you need to transfer amount greater than 0")
                form = forms.MoneyTransferForm()
                context = {'form': form}
                return render(request,"customers/transaction.html",context)
            if userr == None:
                messages.error(request, "you need to transfer to the correct email")
                form = MoneyTransferForm()
                context = {'form': form}
                return render(request, "customers/transaction.html",context)
            
            form.save()
            user.save()
            userr.save()
            messages.success(request,"Transaction Successfull")
            form = MoneyTransferForm()
            context = {'form': form}
            return render(request,"customers/transaction.html",context)
        else:
            messages.error(request,"you need to give proper details in the fields")
            form = MoneyTransferForm()
            context = {'form': form}
            return render(request,"customers/transaction.html",context)
    else:
        form = MoneyTransferForm()
        context = {'form':form}
        return render(request, "customers/transaction.html",context)

def view_hist(request):
    hists = Hist.objects.all()
    return render(request,"customers/hist_details.html",{'hists' : hists })







