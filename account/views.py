from django.forms import PasswordInput
from django.shortcuts import render , redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages





# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']
        user = User.objects.create_user(username=username, email=email, password=Password1, first_name=first_name, last_name=last_name)
        user.save();
        print("user created ")
        return render(request, 'main/home1.html', {'user_created': True})
    else:

        return render(request , 'main/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password= password)

        if user is not None:
            auth.login(request,user)
            return render(request , 'main/home1.html')
        else:
            messages.info(request, 'invalid credentials')
            return render(request,'main/login.html')
    else:
      return render(request , 'main/login.html')


def logout(request):
         auth.logout(request) 
         return render(request , 'main/home1.html') 


# def plane(request):
#     if request.method =='POST':
#         Email = request.POST.get('register.email','')
#         first_name= request.POST.get('register.first_name','')
#         last_name= request.POST.get('register.last_name','')
#         adults= int(request.POST('adults',''))
#         children=int(request.POST('children',''))
#         price = int(request.POST('tp',''))
#         booking = Booking(Email = Email,First_Name = first_name,Last_name = last_name,adults=adults,children=children,price=price)
#         booking.save();
#         print("Booking_successful")
#         return render(request, 'main/plane.html', {'Booking_successful': True})
#     else:
#         print('page_is_notworking')
#         return render(request , 'main/home1.html',{'page_is_notworking': True})


