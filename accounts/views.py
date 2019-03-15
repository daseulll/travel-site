from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('root')
        
    else: 
        form = SignupForm()

    return render(request, "accounts/signup.html", {
        "form" : form,
    })

def signin(request):
    ctx={}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('root')
        else:
            ctx.update({"fail" : "가입되어 있지 않거나 비밀번호가 틀렸습니다."})
    return render(request,"accounts/signin.html", ctx)

def signout(request):
    logout(request)
    return redirect ('root')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {})

@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)

    
    else:
        form = ProfileForm()
        return redirect('profile')

    return render(request, 'accounts/profile_form.html', {})