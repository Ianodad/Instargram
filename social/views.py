from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, Comment
from .forms import ProfileForm, CommentForm, PostForm
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    word = "Hello Instargram"

    
    
    return render(request, "socials/home.html", {"word": word, "form":form })


def profile(request):
    profile = "These is a profile"
    return render(request, "socials/profile.html", {"profile": profile})


def add_photo(request):
    newit = "This is a model"
    current_user = request.user
    
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.User = current_user
            form.save()
    else: 
        form = ProfileForm()
    return render(request, "navbar.html", {"newit": newit, "form": form })




