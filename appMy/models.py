from django.db import models

# Create your models here.

class Contents(models.Model):
    title = models.CharField(("Film Adı"), max_length=50)
    slug =  models.SlugField(("Tür"), null=True)
    image = models.ImageField(("Resim"), upload_to="contents", max_length=None)
    isnew = models.BooleanField(("Yeni Eklenmiş"), default=False)
    ispopular = models.BooleanField(("Popüler"), default=False)
    def __str__(self):
        return self.title