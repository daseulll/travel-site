from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    ctx ={}
    return render(request, "blog/index.html", ctx)

def signup(request):
    ctx={}
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(username, email, password)
        if User.objects.filter(username=username).exists():
            ctx.update({"exist" : "사용중인 아이디입니다."})
        elif User.objects.filter(email=email).exists():
            ctx.update({"e_exist" : "이미 가입하신 이메일입니다."})
        else:
            user = User.objects.create_user(username, email, password)
            ctx.update({"complete" : "회원가입이 완료되었습니다."})

    return render(request, "blog/signup.html", ctx)

def signin(request):
    ctx={}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            ctx.update({"fail" : "가입되어 있지 않거나 비밀번호가 틀렸습니다."})
    return render(request,"blog/signin.html", ctx)

def signout(request):
    logout(request)
    return redirect ('/')

def post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(author=request.user)

    return render(request, "blog/post_list.html", {'posts':posts})

def post_detail(request, post_id):
    # post = get_object_or_404(Post, pk=post_id)
    if request.method == "GET":
        post = Post.objects.get(pk=post_id)

    return render(request, "blog/post_detail.html", {'post':post})

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

def post_draft_list(request):
    draft_posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, "blog/post_list.html", {"draft_posts":draft_posts})

def post_publish(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.publish()
    return redirect('post_detail', post_id)

def post_delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('post_list')
