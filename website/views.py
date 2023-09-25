from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, AddRecordForm
from .models import Record
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



def home(request):
    # Check if user is authenticated before filtering records
    if request.user.is_authenticated:
        records = Record.objects.filter(user=request.user)
    else:
        records = None

    return render(request, 'home.html', {'records': records})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again or sign up.")
            return redirect('home')

    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have been successfully registered.")
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

#def add_record(request):
    #messages.success(request, "you can add record below")
    #return render(request, 'add_record.html', {})

# record added defination
@login_required
def add_record(request):
    messages.success(request, "you can add a record below")

    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            # Get the logged-in user and set it as the user of the record
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = AddRecordForm()

    return render(request, 'add_record.html', {'form': form})


@login_required
def update_record(request):
    user = request.user
    records = Record.objects.filter(user=user)

    if request.method == 'POST':
        selected_record_id = request.POST.get('record_id')
        record = get_object_or_404(Record, pk=selected_record_id)
        form = AddRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the name of the view you want to redirect after updating the record
    else:
        form = AddRecordForm()

    return render(request, 'update_record.html', {'form': form, 'records': records})
