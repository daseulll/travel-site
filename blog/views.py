from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

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
        posts = Post.objects.filter(id=post_id)

    return render(request, "blog/post_detail.html", {'posts':posts})
