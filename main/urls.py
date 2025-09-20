from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('api/banner', views.banner, name='banner_api'),
  path('api/sellers', views.sellers, name='sellers_api'),
]