from django.shortcuts import render , HttpResponse
from home.models import Contact
# Create your views here.
def index(request):
    return render(request , "index.html")
    # return HttpResponse("index.html")

def about(request):
    return render(request,"about.html")
    # return HttpResponse("This is about Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        contact = Contact(name=name , email=email, phone=phone)
        contact.save()
    return render(request,"contact.html")
    # return HttpResponse("This is contact Page")

def services(request):
    return render(request,"services.html")
    # return HttpResponse("This is services Page")