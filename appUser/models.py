from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Userinfo(models.Model):
    user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    tel = models.CharField(("Telefon"), max_length=50, default="", blank=True)
    # adress = models.TextField(("Adres"))
    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Başlık"), max_length=50)
    image = models.ImageField(("Profil Resmi"), upload_to="profile", max_length=None)
    isview = models.BooleanField(("Görüntüleme"), default=True)
    islogin = models.BooleanField(("Girişli Kullanıcı"), default=False)
    def __str__(self):
        return self.title
    
class Emailmessage(models.Model):
    title = models.CharField(("Konu"), max_length=50)
    text = models.TextField(("Mesaj"))
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title