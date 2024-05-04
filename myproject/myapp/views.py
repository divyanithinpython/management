from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,loader,HttpResponse
from.models import*
from.forms import*
from django.contrib.auth import login,logout

from django.contrib.auth import authenticate

# Create your views here.
def Index(request):
  return render(request,'index.html')
def tour(request,):
    return render(request,'tourpackage.html')
def package_location_detail(request,location):
    queryset=Pakage.objects.filter(location)

    return render(request,'packge_details.html',{'queryset':queryset})


def packagedetail(request):
    package=Pakage.objects.all()
    
    return render(request,'packge_details.html',{'package':package})


def add_package(request):
    if request.method=='POST':
        form=Package_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('packagedetail')
    else:

        form=Package_Form()
    return render(request,'addpackage.html',{'form':form})
def registerpage(request):
    return render(request,'register.html')


def useregister(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['Username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user=UserRegister.objects.filter(Email=email)
        if user:
             message="User already exist"
             return render(request,"register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser=UserRegister.objects.create(Firstname=fname,Lastname=lname,Username=username,Email=email,Password=password,ConfirmPassword=cpassword)
                message="User register successfully"
                return render(request,"login.html",{'msg':message})
    else:
          
          return render(request,"register.html")
    

def user_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        user=UserRegister.objects.get(Email=email)
        if user:
            if user.Password==password:
                return render(request,"index.html")
    else:
          
        return render(request,"login.html")
            
def vendorregister(request):
    if request.method=="POST":
        vname=request.POST['vname']
        
        email=request.POST['email']
        
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user=VendorRegister.objects.filter(Email=email)
        if user:
             message="User already exist"
             return render(request,"vendor_register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser=VendorRegister.objects.create(Vendorname=vname,Email=email,Password=password,ConfirmPassword=cpassword)
                message="User register successfully"
                return render(request,"vendor_login.html",{'msg':message})
    else:
          
          return render(request,"vendor_register.html")
def vendorlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        user=VendorRegister.objects.get(Email=email)
        if user:
            if user.Password==password:
                return render(request,"home.html")
    else:
          
        return render(request,"vendor_login.html")
    

def home(request):
    return render(request,'home.html')


def payment(request):
 us=TravelBook.objects.all()
 return render(request,'payment.html',{'us':us})

def book(request):
    if request.method=='POST':
        form=Booking_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('payment')
    else:

        form=Booking_Form()
    return render(request,'book.html',{'form':form})
def confirmlist(request):
  us=TravelBook.objects.all
  return render(request,'confirmation.html',{'us':us})


    
     
        

    




    

            