from django.shortcuts import render ,HttpResponse
from app.models import Contact
import json
# Create your views here.

def home(request):
    return render(request , 'home.html')
def about(request):
    return render(request , 'about.html')

def project(request):
    return render(request , 'project.html')

def contact(request):
    if request.method=="POST":
        print("Here")
        # x = json.loads(request.body)
        # print (x)
        name= request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        # des=request.POST['des']
        print(name,email,phone)
        ins=Contact(name= name ,email= email,phone=phone)
        ins.save()
        print("data has daves")
 

    return render(request , 'contact.html')  
