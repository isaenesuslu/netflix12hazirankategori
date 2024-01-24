from django.shortcuts import render
from appMy.models import *
from appUser.models import Profile
from django.db.models import Q

# Create your views here.


def indexPage(request):
   context = {}
   return render(request, "index.html", context)
   
def browseindexPage(request):
   
   profile = Profile.objects.get(user=request.user, islogin=True)
   
   
   content_list = Contents.objects.all()
   
   context = {
      "profile":profile,
      "content_list":content_list,
   }
   return render(request, "browse-index.html", context)

def categoryPage(request, slug):
   
   content_list = Contents.objects.filter(slug=slug)
   
   if request.path == "/netflix/yeni-ve-populer":
    content_list =  Contents.objects.filter(Q(isnew=True) | Q(ispopular=True))
   
   context = {
      "content_list":content_list,
   }
   return render(request, "category.html", context)
