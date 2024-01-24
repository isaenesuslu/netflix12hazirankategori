from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from appUser.models import *
from django.core.mail import send_mail
from netflix12haziran.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required # Decorator: Giriş yapmayanları kısıtlar

# Create your views here.


def emailmessagePage(request):
   
   user_list = User.objects.values("email")
   user_email_list = []
   for i in user_list:
      user_email_list.append(i["email"])
   
   if request.method == "POST":
      title = request.POST.get("title")
      text = request.POST.get("text")
      
      emailmessage = Emailmessage(title=title,text=text)
      emailmessage.save() # SQL kayıt
      
      for i in user_email_list:
         send_mail(
            title,
            text,
            EMAIL_HOST_USER,
            [i],
            fail_silently=False,
         )
      
   
   context = {}
   return render(request, 'emailmessage.html', context)

@login_required(login_url="loginPage")
def profilePage(request):
   context = {}
   profile_list = Profile.objects.filter(user=request.user, isview=True)
   submit = request.POST.get("submit")
   if request.method == "POST":
      title = request.POST.get("title")
      image = request.FILES.get("image")
      if submit == "profileCreate":

         if len(profile_list) < 4:    
            if title and image:
                     profile = Profile(title=title, image=image, user=request.user)
                     profile.save()
                     return redirect("profilePage")
            else:
               messages.warning(request, "Boş bırakılan yerler var")
      elif submit == "profileUpdate":
         profileid = request.POST.get("profileid")
         profile = Profile.objects.get(user=request.user, id=profileid)
         if title:
            profile.title = title
            profile.save()
            return redirect("profilePage")
         if image:   
            profile.image = image
            profile.save()
            return redirect("profilePage")
         
         
         
          
   context.update({
      "profile_list":profile_list,
   })
   return render(request, "profile.html", context)
   
@login_required(login_url="loginPage")   
def profileDelete(request, pid):
   profile = Profile.objects.get(user=request.user, id=pid)
   profile.isview = False
   profile.save()
   return redirect("profilePage")
   
@login_required(login_url="loginPage")   
def profileLogin(request, pid):
   
   profile_list = Profile.objects.filter(user=request.user) # Kullanıcının tüm profilleri
   profile_list.update(islogin=False) # Tüm listedeki objelerin islogin False olsun
   
   profile = Profile.objects.get(user=request.user, id=pid) # Tıklanan profil
   profile.islogin= True # Girişli olarak ayarla
   profile.save() # Kaydet
   return redirect("browseindexPage")

   # ===================================================================
@login_required(login_url="loginPage")   
def hesapPage(request):
   profile = Profile.objects.get(user=request.user, islogin=True)
   if request.method == "POST":
      submit = request.POST.get("submit")
      
      if submit == "emailSubmit":
         email = request.POST.get("email")
         password = request.POST.get("password")
         # set_password() - Şifreyi değiştirir
         # check_password - Şifreyi kontrol eder
         if request.user.check_password(password): # True ya da False
            request.user.email = email
            request.user.save()
            return redirect("hesapPage")
         else:
            messages.error(request, "Şifreniz yanlış, email değiştirilemedi.")
      elif submit == "passwordSubmit":
         password = request.POST.get("password")
         password1 = request.POST.get("password1")
         password2 = request.POST.get("password2")
         if request.user.check_password(password):
            if password1 == password2:
               request.user.set_password(password1)
               request.user.save()
               return redirect("loginPage")
            else:
               messages.error(request, "Yeni şifreler birbiriyle uyuşmuyor.")
         else:
            messages.error(request, "Şifreniz yanlış, şifre değiştirilemedi.")
      elif submit == "telSubmit":
         tel = request.POST.get("tel")         
         password = request.POST.get("password")         
         if request.user.check_password(password):
            request.user.userinfo.tel = tel
            request.user.userinfo.save()
            return redirect("hesapPage")
         else:
            messages.error(request, "Şifreniz yanlış, telefon numarası değiştirilemedi.")
   
   context = {
      "profile":profile
   }
   return render(request, "hesap.html", context)
   
def loginPage(request):
   
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      rememberme = request.POST.get("rememberme")
      
      user = authenticate(username = username, password = password)
      if user:
         login(request,user)
         
         if rememberme:
            request.session.set_expiry(604800) # 1 Haftaya tekabül ediyor.
         return redirect("profilePage")
      else:
         messages.error(request, "Kullanıcı adı veya şifre yanlış!")
         
   
   context = {}
   return render(request, "user/login.html", context)
   
def registerPage(request):
   context = {}
   
   if request.method == "POST":
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")
      
      site = request.POST.get("check-site")
      kvkk = request.POST.get("check-kvkk")
      
      if fname and lname and email and username and password1 and site and kvkk:
         if password1 == password2:
            if not User.objects.filter(username=username).exists():
               if not User.objects.filter(email=email).exists():
                  
                  # Password control
                  num_bool = up_bool = False
                  
                  for k in password1:
                     if k.isnumeric(): num_bool = True
                     if k.isupper(): up_bool = True
                  
                  if len(password1)>=8 and num_bool and up_bool:
                     user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password1)
                     user.save()     
                     return redirect("loginPage")   
                  else:
                     messages.error(request, "Şifrenizin uzunluğu 8 veya daha uzun olmak zorunda!")
                     messages.error(request, "Şifrenizde en az bir rakam olmak zorunda!")
                     messages.error(request, "Şifrenizde en az bir büyük harf olmak zorunda!")
               else:
                  messages.error(request, "Bu mail zaten kullanılıyor!")
            else:
               messages.error(request, "Kullanıcı adı daha önceden alınmış")
         else:
             messages.error(request, "Şifreler Aynı değil!")    
      else:
            messages.warning(request, "Boş bırakılan yerleri lütfen doldurunuz.")
            context.update({"fname":fname,"lname":lname,"username":username,"email":email})
   return render(request, "user/register.html", context)

@login_required(login_url="loginPage")
def logoutUser(request):
   logout(request)
   return redirect("loginPage")   
