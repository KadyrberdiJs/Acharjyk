from re import S
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from rest_framework import generics, status
from rest_framework.response import Response

from main.models import Banner, Sellers
from main.serializer import BannerSerializer, SellersSerializer


# Banner 
class BannerList(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def delete(self, request, *args, **kwargs):
        Banner.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_serializer_context(self):
        return {'request': self.request}

class BannerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    lookup_field = 'pk'

    def get_serializer_context(self):
        return {'request': self.request}
    

# Seller 

class SellerList(generics.ListCreateAPIView):
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
