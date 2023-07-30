"""
Writing all website app views
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUser, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    """home view function"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticating the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect("dashboard")
        messages.success(
            request, "An Error Occurred While Trying To Login, Please Try Again"
        )
        return redirect("home")
    return render(request, "home.html", {})


def dashboard(request):
    """function returning the dashboard"""
    records = Record.objects.all()
    return render(request, "dashboard.html", {"records": records})


def logout_user(request):
    """logout function"""
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("home")


def register_user(request):
    """registration function"""
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully")
            return redirect("home")
    else:
        form = RegisterUser()
    return render(request, "registration.html", {"form": form})


def customer_record(request, pk):
    """customer record view function"""
    if request.user.is_authenticated:
        # view record
        client_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"client_record": client_record})
    messages.success(request, "You must be logged in to access customer records")
    return redirect("home")


def delete_record(request, pk):
    """delete function"""
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted Successfully")
        return redirect("dashboard")
    else:
        messages.success(request, "You have to be logged in to delete a record")
        return redirect("home")


def add_record(request):
    """add record function"""
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added successfully")
                return redirect("dashboard")
        return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "You must be logged in to add a record")
        return redirect("home")
    
def update_record(request, pk):
    """Updating record function"""
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect("dashboard")
        return render(request, "update_record.html", {"form": form})
    messages.success(request, "You must be logged in to add a record")
    return redirect("home")
