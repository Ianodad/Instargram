from urllib import request

from .forms import CommentForm, PostForm, ProfileForm
from .models import Comment, Post, Profile, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from django.db.models import Q

# Create your views here.


@login_required(login_url='/accounts/login/')
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
    # print((posts[1].comments.all()))
    return render(request, 'socials/home.html', {"word": word, "form": form, "posts": posts})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.name = current_user
            upload.save()
            return redirect('profile')

    else:
        formit = ProfileForm()
    posts = Post.get_post(current_user)
    profile = Profile.get_profile(current_user)
    return render(request, "socials/profile.html", {"profile": profile, "formit": formit, "posts": posts})


@login_required(login_url='/accounts/login/')
def comment(request, post_id):

    current_user = request.user
    posts = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posts = posts
            comment.user = current_user
            comment.save()
        return redirect('home')

    # else:
    #     commentform = ProfileForm()
    # return render(request, "'socials/home.html'", {"newit": newit})


@login_required(login_url='/accounts/login/')
def search(request):
    query = request.GET.get('q')
    print(query)
    if query:
        results = Projects.objects.filter(
            Q(user__icontains=query))
    else:
        results = Post.objects.all()

    return render(request, 'socials/search.html', { "profiles": profile, "results":results})
