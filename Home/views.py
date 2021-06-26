from django.shortcuts import render,HttpResponse,redirect
#importing UserDetails from .models
from .models import UserDetails
from django.views.generic import View

#rendering home page
def index(request):
    return render(request,"index.html")
#renderong balenced diet page
def diet(request):
    return render(request,"diet.html")

def login(request):
#defined global variables to give them a value of 0 if they are not given by user they will be 0 by default
    totalCals=totalProt=totalCals1=totalProt1=totalCals2=totalProt2=totalCals3=0
    if(request.method == 'POST'):
#if some one is logging in first time
       if 'login' in request.POST:
#making a varibales and getting them from database
            email = request.POST.get("email")
            password = request.POST.get("password")
#getting the email of user if exists from data base
            object = UserDetails.objects.get(email=email)
#if password exists we retrive it from data base
            if(password == object.password):
                return render(request,"login.html", {'login':"login"})
#if it doesn't exist we render the login page back again
            else:
                return render(request,"login.html")
#if the user is logged in we render the login.html again
       else:
           lists = ["carb","grams","prot","grams1","carblun","grams2","protlun","grams3","carbdin","grams4","protdin","grams5","carbsnack","grams6","tarcarb","tarprot"]            
           for i in lists:
               globals()[i]=request.POST.get(i)
#the string from the lists is stored in a dictionary and a value is added to it when try to retrive the value of string it retuns the value stored in key
           carbohydrate = {"bread":49, "roti":264 , "idli": 360 , "oats": 68}
           protiene = {"egg":13,"sausages":27,"milk":3.4,"yogurt": 10}
           carbohydrate1 = {"rice":28,"chapati":264,"pumpkin":70,"curd":10}
           protiene1 = {"sprouts":3.4,"boiledegg":13,"paneer":20,"yougurt":10}
           carbohydrate2 = {"rice":28,"chapati":264,"pumpkin":70,"curd":10}
           protiene2 = {"sprouts":3.4,"boiledegg":13,"paneer":20,"yougurt":10}
           carbohydrate3 = {"coke":40,"lays":547,"maggi":97,"orange":47}
#if carb exists in carbohydrate the if condition works 
           if carbohydrate.get(carb):
               totalCals = int(grams)/100 *carbohydrate.get(carb)
           if protiene.get(prot):
              totalProt = int(grams1)/100 *protiene.get(prot)
           if carbohydrate1.get(carblun):
               totalCals1 = int(grams2)/100 *carbohydrate1.get(carblun)
           if protiene1.get(protlun):
               totalProt1 = int(grams3)/100 *protiene1.get(protlun)
           if carbohydrate2.get(carbdin):
               totalCals2 = int(grams4)/100 *carbohydrate2.get(carbdin)
           if protiene2.get(protdin):
               totalProt2 = int(grams5)/100 *protiene2.get(protdin)
           if carbohydrate3.get(carbsnack):
               totalCals3 = int(grams6)/100 *carbohydrate3.get(carbsnack)
#passing the context         
           context = { "calories":totalCals,"protiens":totalProt,"calorieslunch":totalCals1,"protienslunch":totalProt1,"caloriesdinner":totalCals2,
           "protiensdinner":totalProt2,"carloriessnack":totalCals3,"totalcarbs":totalCals+totalCals1+totalCals2+totalCals3,"totalprotiens":totalProt+totalProt1+totalProt2}
#handiling the errors
           try:
               if tarcarb!=None and int(tarcarb)<totalCals+totalCals1+totalCals2+totalCals3:
                   context["usercarb"] = "Exceeded"
               if tarcarb!=None and int(tarcarb)>totalCals+totalCals1+totalCals2+totalCals3:
                   context["usercarb"] = "Not Exceeded"
           except:
               return HttpResponse("Entre the target value for Carbohydrates")
           try:
               if tarprot!=None and int(tarprot)<totalProt+totalProt1+totalProt2:
                   context["userprot"] = "Exceeded"
               if tarprot!=None and int(tarprot)>totalProt+totalProt1+totalProt2:
                   context["userprot"] = "Not Exceeded"
           except:
               return HttpResponse("Entre the traget value for Protiens")
 
           return render(request,"result.html",context)

    else:
        return render(request,"login.html")

#signup page
def signup(request):

    if(request.method == 'POST'):
           email = request.POST.get("email1")
           password = request.POST.get("password1")
           passwordverif = request.POST.get("passwordverif")
           UserDetails.objects.create(email=email,password=password)
           return redirect("login")

    else:
        return render(request,"signup.html")

#defininig the bmr page
def bmr(request):
    Bmr=0
    if(request.method == 'POST'):
        lists=["age","gender","height","weight"]
        for i in lists:
            globals()[i]=request.POST.get(i)
        context={}
        if gender=="male":
            Bmr=10*int(weight)+6.25*int(height)-5*int(age)+5
            context["result"]=Bmr
        if gender=="female":
            Bmr=10*int(weight)+6.25*int(height)-5*int(age)-161
            context["result"]=Bmr
#passing the context depending on choosen option to new.html
        return render(request,"new.html",context)
    else:
        return render(request,"bmr.html")

