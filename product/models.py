from django.db import models

class Category(models.Model):
   name = models.CharField(max_length=200, unique=True, verbose_name='Имя')
   slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
   image = models.ImageField(upload_to='category_images', verbose_name='Изображения')


   class Meta:
    db_table = 'category'
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
  
   def __str__(self):
      return self.name

class Product(models.Model):
  name = models.CharField(max_length=200, unique=True, verbose_name='Имя')
  slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
  creater = models.CharField(max_length=200, verbose_name='Создатель')
  category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='products',
                               verbose_name='Категория')
  file = models.FileField(upload_to='product-files/')
  downloads = models.PositiveBigIntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
     db_table = 'product'
     verbose_name = 'Продукт'
     verbose_name_plural = 'Продукты'
     ordering = ('-created_at',)

  def __str__(self):
      return self.name



   
