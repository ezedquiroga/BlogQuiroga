from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from Account.forms import UserRegisterForm


def login_account (request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user:
                login(request, user)

                return redirect("AplicacionAdopcion")
            else:
                return redirect("home")

    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "Account/login.html", context=context)


def register_account(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("AccountLogin")

    form = UserRegisterForm()
    context = {
        "form":form
    }
    return render(request, "Account/login.html", context=context)