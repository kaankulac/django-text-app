from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('Giriş başarılı')
            return redirect('main')
    else:
        return render(request,'user/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['psw-repeat']
        name = request.POST['name']
        surname = request.POST['surname']
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                print('Kullanıcı adı daha önce alınmış.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('Email zaten kullanımda.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=name,last_name=surname,email=email)
                user.save()
                print('Kayıt başarılı')
                return redirect('login')

        else:
            print('Şifreler uyuşmuyor.')
            return redirect('register')
       
    else:
        return render(request,'user/register.html') 
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        print('Çıkış yapıldı..')
        return redirect('login')