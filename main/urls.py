from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('api/banner', views.BannerList.as_view(), name='banner_api'),
  path('api/banner/<int:pk>', views.BannerRetrieveUpdateDestroy.as_view(),
        name='banner_update'),
  path('api/sellers', views.SellerList.as_view(), name='sellers_api'),
]
