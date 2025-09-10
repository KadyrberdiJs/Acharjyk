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