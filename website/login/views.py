# coding=utf-8

# Create your views here.

from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from login.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout


# 定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

# 登录


def login_view(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            #user = User.objects.filter(username__exact = username,password__exact = password)
            user = authenticate(username=username, password=password)
            print username,password
            print user
            if user is not None:
                print user.is_active
                if user.is_active:
                    login(request, user)
                    return render_to_response('success.html', {'username': username})
            else:
                    #return render_to_response('success.html', {'username': username})
                    return HttpResponseRedirect('/login/')

        else:
            pass
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})


def sign_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('success.html', {'username': username})
            else:
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')
    return render_to_response('sign_in.html')