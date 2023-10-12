from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# from .models import ExpenseModel
from income.models import IncomeModel
from expense.models import ExpenseModel

def home(request):
    return render(request, "home.html")

def adduser(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        uemail = request.POST.get("email")
        upassword = request.POST.get("password")
        
        # Corrected line: Use the actual password provided by the user
        obj = User.objects.create_user(username=uname, email=uemail, password=upassword)
        obj.save()
        return redirect("/Account/adduser")
    else:
        return render(request, "form.html")

def loginuser(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pswd = request.POST.get("upassword")
        user = authenticate(request, username=uname, password=pswd)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            d = {"msg": "Invalid username and password"}
            return render(request, "login.html", d)
    else:
        return render(request, "login.html")

def logot(request):
    logout(request)
    return redirect('/')


# def signout(request):
#     pass

def srch(request):
    uid=request.session.get("_auth_user_id")
    obj=User.objects.get(id=uid)
    srchdata=request.GET.get('srch')
    datai=IncomeModel.objects.filter(income_description__contains=srchdata,user=obj)
    datae=ExpenseModel.objects.filter(expense_description__contains=srchdata,user=obj)
    d={
        "data1": datai,
        "data2": datae

    }
    return render(request,"srch.html",d)
