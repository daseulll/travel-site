from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

LOGIN_URL = "/signin/"

def index(request):
    if request.method == "GET":
        posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts" : posts})


@login_required(login_url=LOGIN_URL)
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(author=request.user)

    return render(request, "blog/post_list.html", {'posts':posts})

@login_required(login_url=LOGIN_URL)
def post_detail(request, post_id):
    # post = get_object_or_404(Post, pk=post_id)
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)
    return render(request, "blog/post_detail.html", {'post':post})

@login_required(login_url=LOGIN_URL)
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()

    return render(request, "blog/post_edit.html", {'form' : form})

@login_required(login_url=LOGIN_URL)
def post_edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_id )
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_edit.html", {'form' : form})

@login_required(login_url=LOGIN_URL)
def post_draft_list(request):
    draft_posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, "blog/post_list.html", {"draft_posts":draft_posts})

@login_required(login_url=LOGIN_URL)
def post_publish(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.publish()
    return redirect('post_detail', post_id)

@login_required(login_url=LOGIN_URL)
def post_delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id)
    else:
        form = CommentForm()

    return render(request, "blog/add_comment_to_post.html", {"form":form})

@login_required
def comment_approve(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.approve()
    return redirect('post_detail', comment.post.id)

@login_required
def comment_remove(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('post_detail', comment.post.id)
