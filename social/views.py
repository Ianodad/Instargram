from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, Comment
from .forms import ProfileForm, CommentForm, PostForm
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    word = "Hello Instargram"

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
    else:
        form = PostForm()
    
    return render(request, "socials/home.html", {"word": word})


def profile(request):
    profile = "These is a profile"
    return render(request, "socials/profile.html", {"profile": profile})


def add_photo(request):
    newit = "This is a model"
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)


    return render(request, "navbar.html", {"newit": newit})

