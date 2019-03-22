from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm
from .models import Profile

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            next_url = request.GET.get('next') or 'root'
            return redirect(next_url)
    else: 
        form = SignupForm()

    return render(request, "accounts/signup.html", {
        "form" : form,
    })

def signin(request):
    ctx = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or 'root'
            return redirect(next_url)
        else:
            ctx.update({"fail" : "가입되어 있지 않거나 비밀번호가 틀렸습니다."})
    return render(request, "accounts/signin.html", ctx)

def signout(request):
    logout(request)
    return redirect('root')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {})

@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    print(profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_form.html', {"form":form})
