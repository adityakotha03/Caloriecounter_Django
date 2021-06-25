from django.shortcuts import render,HttpResponse
from .models import UserDetails
from django.views.generic import View
 
#importing get_template from loader
from django.template.loader import get_template
 
#import render_to_pdf from util.py 
from .utils import render_to_pdf 

def index(request):
    return render(request,"index.html")

def diet(request):
    return render(request,"diet.html")

def login(request):
    totalCals=totalProt=totalCals1=totalProt1=totalCals2=totalProt2=totalCals3=0

    if(request.method == 'POST'):

       if 'login' in request.POST:

            email = request.POST.get("email")
            password = request.POST.get("password")
            object = UserDetails.objects.get(email=email)

            if(password == object.password):
                return render(request,"login.html", {'login':"login"})

            else:
                return render(request,"login.html")
       else:
           carb = request.POST.get('carb')
           grams = request.POST.get('grams')
           prot = request.POST.get('prot')
           grams1 = request.POST.get('grams1')
           carblun = request.POST.get('carblun')
           grams2 = request.POST.get('grams2')
           protlun = request.POST.get('protlun')
           grams3 = request.POST.get('grams3')
           carbdin= request.POST.get('carbdin')
           grams4 = request.POST.get('grams4')
           protdin = request.POST.get('protdin')
           grams5 = request.POST.get('grams5')
           carbsnack= request.POST.get('carbsnack')
           grams6 = request.POST.get('grams6')
           tarcarb = request.POST.get('tarcarb')
           tarprot = request.POST.get('tarprot')


           carbohydrate = {"bread":49, "roti":264 , "idli": 360 , "oats": 68}
           protiene = {"egg":13,"sausages":27,"milk":3.4,"yogurt": 10}
           carbohydrate1 = {"rice":28,"chapati":264,"ptarprotumpkin":7,"curd":10}
           protiene1 = {"sprouts":3.4,"boiledegg":13,"paneer":20,"yougurt":10}
           carbohydrate2 = {"rice":28,"chapati":264,"pumpkin":7,"curd":10}
           protiene2 = {"sprouts":3.4,"boiledegg":13,"paneer":20,"yougurt":10}
           carbohydrate3 = {"coke":40,"lays":547,"maggi":97,"orange":47}

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

              
           context = {}
           context["calories"] = totalCals
           context["protiens"] = totalProt
           context["calorieslunch"] = totalCals1
           context["protienslunch"] = totalProt1
           context["caloriesdinner"] = totalCals2
           context["protiensdinner"] = totalProt2
           context["carloriessnack"] = totalCals3
           context["totalcarbs"] = totalCals+totalCals1+totalCals2+totalCals3
           context["totalprotiens"] = totalProt+totalProt1+totalProt2

           
           if tarcarb==None:
               context["usercarb"] = "Not Given"
           elif tarcarb!= None and int(tarcarb)<totalCals+totalCals1+totalCals2+totalCals3:
               context["usercarb"] = "Exceeded"
           elif tarcarb!= None and int(tarcarb)>totalCals+totalCals1+totalCals2+totalCals3:
               context["usercarb"] = "Not Exceeded"
           if tarprot==None:
               context["userprot"] = "Not Given"
           elif tarprot!= None and int(tarprot)<totalProt+totalProt1+totalProt2:
               context["userprot"] = "Exceeded"
           elif tarprot!= None and int(tarprot)>totalProt+totalProt1+totalProt2:
               context["userprot"] = "Not Exceeded"
 
           return render(request,"result.html",context)

    else:
        return render(request,"login.html")


def signup(request):

    if(request.method == 'POST'):
           email = request.POST.get("email1")
           password = request.POST.get("password1")
           passwordverif = request.POST.get("passwordverif")
           UserDetails.objects.create(email=email,password=password)
           return render(request,"login.html")

    else:
        return render(request,"signup.html")

class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        #getting the template
        pdf = render_to_pdf('result.html')
         
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
        #and