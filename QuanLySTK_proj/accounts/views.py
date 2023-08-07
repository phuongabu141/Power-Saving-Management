from django.shortcuts import render
from django.contrib.auth.decorators import login_required # add login and permission required decorator
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as django_logout
from admin_site import models


decorator_with_arguments = lambda decorator: lambda *args, **kwargs: lambda func: decorator(func, *args, **kwargs)

@decorator_with_arguments
def custom_permission_required(function, perm):
    def _function(request, *args, **kwargs):
        if request.user.has_perm(perm):
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'Bạn không có quyền truy cập vào trang này')
            return redirect('accounts:signin')
    return _function

#@login_required()
# class MyPasswordChangeView(PasswordChangeView):
#     form_class = PasswordChangeForm
#     template_name = 'accounts/change_password.html'
#     success_url = '/accounts/signin'

# Create your views here.
def signin(request):
    if request.method == "POST":
        username = request.POST.get('tendangnhap')
        password = request.POST.get('matkhau')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_active:
                if user.is_superuser==False and user.is_staff==False:
                    login(request,user)
                    
                    return redirect('normal_site:home',username) # điều hướng về trang chủ
                else:
                    login(request,user)
                    return redirect('/admin/') # điều hướng về admin
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('accounts:signin')

    return render(request,"accounts/login.html")

@login_required()
@custom_permission_required('admin_site.add_authuser')
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        position = request.POST.get('position', False)

        # Xử lý mã nhân viên
        manv = 'NV' + str(int(models.Thamso.objects.get(tenthamso='SLNguoiDung').giatri)+1)

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return redirect('adsite:signup')
            else:
                user = User.objects.create_user(username=username,password=password1,first_name=name,email=email)
                user.first_name = name # first name equal full name
                user.save()

                user_extend= models.UsersExtendClass.objects.create(user=user,manv=manv)
                user_extend.save()

                if position == "NhanVien":
                    group = Group.objects.get(name='NhanVien')
                    user.groups.add(group)

                if position == "NhanVienPhanTichDuLieu":
                    group = Group.objects.get(name='NhanVienPhanTichDuLieu')
                    user.groups.add(group)

                if position == "GiamDoc":
                    group = Group.objects.get(name='GiamDoc')
                    user.groups.add(group)
                    user.is_staff = True
                    user.save()
                
                models.Thamso.objects.filter(tenthamso='SLNguoiDung').update(giatri=str(int(models.Thamso.objects.get(tenthamso='SLNguoiDung').giatri)+1))
                messages.success(request,"You are registered successfully")
                return redirect('accounts:signin')
        else:
            messages.error(request,"Password not matched")
            return redirect('accounts:signup')

    return render(request,"accounts/register.html")

def reset_password(request,*args, **kwargs):
    return render(request,"accounts/reset_password.html")

@login_required()
def logout (request):
    django_logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('accounts:signin')