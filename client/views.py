from .models import RetailUser
from django.shortcuts import render, redirect
from .forms import RetailUserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .backends import RetailUserBackend
from website.views import home

def retail_user_registration(request):
    if request.method == 'POST':
        form = RetailUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have been successfully registered.")
            return render(request, 'profile.html', {'user': user})
            #return redirect('login_client')
    else:
        form = RetailUserRegistrationForm()
    return render(request, 'retail_user_registration.html', {'form': form})


def login_client(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("post taken")
        # Use the custom RetailUserBackend to authenticate
        user = authenticate(request, username=username, password=password)
        print("user made")
        if user is not None and user.RetailUser:
            login(request, user)
            messages.success(request, "Welcome!")
            return render(request, 'profile.html', {'user': user})
        else:
            messages.error(request, "Invalid credentials. Please try again or Register")
            return redirect('login_client')

    return render(request, 'retail_user_login.html')


def logout_client(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')


"""
def login_client(request):
    if request.user.is_authenticated:
        if RetailUser is not None:
            login(request, RetailUser)
            RetailUser.backend = 'path.to.RetailUserBackend'  # Set the backend attribute
            messages.success(request, "Welcome!")
            return render(request, 'profile.html')

    return LoginView.as_view(
        template_name='retail_user_login.html',
        extra_context={'user_type': 'RetailUser'}  # Pass user type to the template
    )(request)

"""
