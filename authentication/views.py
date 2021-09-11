from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def logout_django(request):
    logout(request)
    return render(request, 'login.html')

def login_django(request):
    if request.method == "POST":
        # Login user if the form has been submitted
        password=request.POST.get('password')
        username = request.POST.get('username')
        try:
            # if there is no error then signin the user with given email and password
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect('home')
            else:
                # No backend authenticated the credentials
                return HttpResponse("Invalid credentials. Please try again.")
        except:
            return HttpResponse("We couldn't log you in. Please double check your login info and try again or contact support.")
    else:
        # Show login page if it's a GET response
        return render(request, "login.html")


def register_django(request):
    if request.method == "POST":
        # Login user if the form has been submitted
        email=request.POST.get('email')
        password=request.POST.get('password')
        username = request.POST.get('username')
        # if there is no error then signin the user with given email and password
        print(email, username, password)
        user = User.objects.create_user(email=email, password=password, username=username)
        user.save()

        return HttpResponse(f'Registered with credentials: {email}, {username}, {password}')
        # session_id=user['idToken']
        # request.session['uid']=str(session_id)
        # return render(request,"Home.html",{"email":email})
    else:
        # Show login page if it's a GET response
        return render(request, "register.html")
