from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password , make_password
from .models import Fcuser
# Create your views here.
def login(request):
    

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