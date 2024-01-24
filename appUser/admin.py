from django.contrib import admin
from appUser.models import *

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('user','title','isview','islogin')
    list_editable = ('isview','islogin') # Liste görünümünde değiştirilmesine izin verir
    # list_filter = ('',) Filtreleme
    readonly_fields = ('title',) # Adminde Değiştirilemesin
    search_fields = ('user__username',) # Arama Yap
    # date_hierarchy = '' Tarih çizelgesi
    # ordering = ('',) Sıralama
    

@admin.register(Emailmessage)
class EmailmessageAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('title','date_now')


admin.site.register(Userinfo)