from django.shortcuts import render,HttpResponse
from home.models import contact
from home.models import product
from home.models import dilivary
from home.models import card

# personal ditals class
class user:

    email=" "

# Create your views here.
def index(request):

    
    return render(request,"index.html")

def home(request):
    data=product.objects.all();
    
    return render(request,"home.html",{"data" :data})
        
      
def login(request):

    if request.method=="POST":

    
            
        con=contact.objects.all();
        Password=request.POST.get('password')
        
        email=request.POST.get('email')
        
        user.email=email
        if contact.objects.filter(email=email , password=Password):

            data=product.objects.all();
            
    
            return render(request,"home.html",{"data" :data})
       
        
        else:
            return render(request,"index.html")
    else:
        return render(request,"index.html")

def sineup(request):
    if (request.method=="POST"):

       
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user.email=email
        Contact=contact(email=email,password=password)
        Contact.save()

    data=product.objects.all();
    
    return render(request,"home.html",{"data" :data})


def item(request):
    if (request.method=="POST"):
      
        pid=request.POST.get('pid')
        dat= product.objects.filter(pid=pid)
        return render(request,"product.html",{"dat" :dat})

    data=product.objects.all();
    return render(request,"home.html",{"data" :data})

def order(request):
    if (request.method=="POST"):

       
        pid=request.POST.get('pid2')
        email=request.POST.get('email')
        address=request.POST.get('address')
        quantity=request.POST.get('quantity')
    
        sales=dilivary(pid=pid,email=email,address=address,quantity=quantity)
        sales.save()

    data=product.objects.all();
    
    return render(request,"home.html",{"data" :data})

def addcard(request):
    if (request.method=="POST"):

       
        pid=request.POST.get('pid3')
        email=request.POST.get('email')
        address=request.POST.get('address')
        image=request.POST.get('pimage')
        price=request.POST.get('pcost')
        disc1=request.POST.get('pdesc1')
        disc2=request.POST.get('pdesc2')
    
        sales=card(pid=pid,email=email,address=address,image=image,price=price,disc1=disc1,disc2=disc2)
        sales.save()

    data=product.objects.all();
    
    return render(request,"home.html",{"data" :data})

def aboutus(request):
    
    
    return render(request,"aboutus.html")
        

def mycard(request):
    eml=user.email
    data=card.objects.filter(email=eml)
    
    return render(request,"home.html",{"data" :data})

def electronics(request):
    data=product.objects.all();
    
    return render(request,"electronics.html",{"data" :data})
        

def fmcg(request):
    data=product.objects.all();
    
    return render(request,"fmcg.html",{"data" :data})
        

def buity(request):
    data=product.objects.all();
    
    return render(request,"buity.html",{"data" :data})
        
        
      