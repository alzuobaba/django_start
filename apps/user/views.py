from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend

# Create your views here.
from django.views.generic.base import View

from user.models import UserProfile
from user.forms import LoginForm,RegisterForm

class my_auth(ModelBackend):
    """
    自定义 验证需要继承这个ModelBackend 重写 authenticate
    还需要在setting里修改 一个变量 AUTHENTICATION_BACKENDS  = 'user.views.my_auth'
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username)|Q(email= username))
            if user.check_password(password):
                return user
        except:
            return None


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email',None)
            pass_word = request.POST.get('password',None)
            if UserProfile.objects.filter(email= user_name):
                return render(request, 'register.html', {'register_form': register_form,'msg':'用户已存在'})
            user = UserProfile()
            user.email = user_name
            user.password = make_password(pass_word)
            user.save()
            return render(request,'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form,})



class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', None)
            pass_word = request.POST.get('password', None)
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            # 这里要再加一层验证，因为数据合法的情况下 通不过数据库验证也是白搭
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误','login_form':login_form})

        else:
            return render(request, 'login.html',{'login_form':login_form})

#
# 改用类来处理get post 之类的逻辑
# def user_login(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username', None)
#         pass_word = request.POST.get('password', None)
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {'msg': '密码错误呀，小哥'})
#     elif request.method == 'GET':
#         return render(request,'login.html')