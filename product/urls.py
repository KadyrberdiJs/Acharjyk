from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
  # API's
  path("", views.product, name="product_api"),
  path("category", views.category, name="category_api"),
  path('<int:pk>/download/', views.download_product, name='download_product')
] 

