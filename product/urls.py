from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
  # API's
  path("", views.ProductList.as_view(), name="product_api"),
  path("category", views.CategoryList.as_view(), name="category_api"),
  path("<int:pk>/download/", views.increment_download, name="increment-download"),
] 

