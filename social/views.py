from urllib import request

from .forms import CommentForm, PostForm, ProfileForm
from .models import Comment, Post, Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


# Create your views here.


# @login_required(login_url='/accounts/login/')
def home(request):
    word = "Hello Instargram"

    current_user = request.user

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
            return redirect('home')

    else:
        form = PostForm()

    posts = Post.get_all_posts()

    return render(request, 'socials/home.html', {"word": word, "form": form, "posts": posts})


def profile(request):
    profile = "These is a profile"
    current_user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.name = current_user
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm()

    posts = Post.get_post(current_user)

    return render(request, "socials/profile.html", {"profile": profile, "form": form, "posts": posts})


def comment(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.name = current_user
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm()
    return render(request, "'socials/home.html'", {"newit": newit})


def search(request):
    if 'profiles' in request.GET and request.GET['profiles']:
        search_term = request.GET.get('profiles')
        user = User.objects.filter(username=search_term)
        Profiles = Profile.objects.filter(username=user)
        message = f'{search_term}'

        return render(request, 'search.html', {"message": message, "profiles": profiles})
    else:
        message = "Please search for users"

    return render(request, 'search.html', {"message": message, "profiles": profile})
