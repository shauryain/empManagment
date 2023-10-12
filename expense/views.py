from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import ExpenseModel


def addexpense(request):
    if request.method == "POST":
        amt=request.POST.get("amt")
        type=request.POST.get("type")
        desc=request.POST.get("description")
        date=request.POST.get("date")
        uid=request.session.get("_auth_user_id")
        user_obj=User.objects.get(id=uid)
        
        obji=ExpenseModel()
        obji.expense_amount=amt
        obji.expense_type=type
        obji.expense_date=date
        obji.expense_amount=amt
        obji.expense_description=desc
        obji.user=user_obj
        obji.save()
        return redirect("/")
    else:
        return render(request,"expenseadd.html")
    
def list(request):
    uid=request.session.get("_auth_user_id")
    obj=User.objects.get(id=uid)
    data=ExpenseModel.objects.filter(user=obj)
    d={
        "data":data
    }
    return render(request,"expensedetails.html",d)
