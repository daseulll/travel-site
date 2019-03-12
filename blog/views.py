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
def post_detail(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    if request.method == "GET":
        post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {'post':post})

@login_required(login_url=LOGIN_URL)
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()

    return render(request, "blog/post_edit.html", {'form' : form})

@login_required(login_url=LOGIN_URL)
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk )
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_edit.html", {'form' : form})

@login_required(login_url=LOGIN_URL)
def post_draft_list(request):
    draft_posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, "blog/post_draft_list.html", {
        "draft_posts": draft_posts,
    })

@login_required(login_url=LOGIN_URL)
def post_publish(request, pk):
    post = Post.objects.get(pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk)

@login_required(login_url=LOGIN_URL)
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('blog:post_list')

def add_comment_to_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentForm()

    return render(request, "blog/add_comment_to_post.html", {"form":form})

@login_required
def comment_approve(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.approve()
    return redirect('blog:post_detail', comment.pk)

@login_required
def comment_remove(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect('blog:post_detail', comment.pk)
