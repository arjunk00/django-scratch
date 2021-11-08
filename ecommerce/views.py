from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.models import User, auth

User = get_user_model()


# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'user does not exist, please register')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gender']
        age = request.POST['age']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email already registered')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, phone_no=phone_no, email=email,
                                            first_name=first_name, last_name=last_name, address=address, gender=gender,
                                            age=age)
            user.save()
            print("user created")
            return redirect('login')
    else:
        return render(request, 'register.html')


def shop(request):
    return render(request, 'shop.html')

# def process_regisration(request):
#     return redirect('login')
