from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    word = "Hello Instargram"
    return render(request, "socials/home.html", {"word": word})


def profile(request):
    profile = "These is a profile"
    return render(request, "socials/profile.html", {"profile": profile})


def add_photo(request):
    newit = "This is a model"
    return render(request, "navbar.html", {"newit": newit})
