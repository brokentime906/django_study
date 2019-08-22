from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password , make_password
from .models import Fcuser
from .forms import LoginForm
# Create your views here.
def home(request):
    user_id = request.session.get('user')
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
    return render(request,'home.html')

def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('/')

def login(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')        
    else:
        form = LoginForm()
        
    return render(request,'login.html' , {'form': form})

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method =="POST":
        username = request.POST.get('username' ,None)
        password = request.POST.get('password' ,None)
        re_password = request.POST.get('re_password', None)
        res_data={}

        if not (username and password and re_password) :
            res_data['error'] = '모두 채워주세요'

        elif password != re_password :
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            fcuser =Fcuser(
            username=username,
            password= make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html' ,res_data)