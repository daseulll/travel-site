from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def index(request):
    ctx ={}
    return render(request, "index.html", ctx)

def signin(request):
    ctx={}
    return render(request,"signin.html", ctx)

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
    return render(request, "signup.html", ctx)
