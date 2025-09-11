from django.db import models


class Banner(models.Model):
   title = models.CharField(max_length=200)
   image = models.ImageField(upload_to='banner_images/')
   description = models.TextField(blank=True)
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      verbose_name = 'Баннер'
      verbose_name_plural = 'Баннеры'
      ordering = ('-created_at',) 

   def __str__(self):
       return self.title
   

class Sellers(models.Model):
   name = models.CharField(max_length=200)
   slug = models.SlugField(max_length=200)
   logo = models.ImageField(upload_to='sellers_logos/')
   description = models.TextField(blank=True)
   price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
   contacts = models.CharField(max_length=200)
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      verbose_name = 'Продавец'
      verbose_name_plural = 'Продавцы'
      ordering = ('name',)

   def __str__(self):
       return self.name