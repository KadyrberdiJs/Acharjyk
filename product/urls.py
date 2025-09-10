from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
  # HTML template
  path("", views.product_list, name="product_list"),

  # API's
  path("api/", views.product, name="product"),
  path('<int:pk>/download/', views.download_product, name='download_product')
] 