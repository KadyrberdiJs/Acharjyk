from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from main.models import Banner, Sellers


@require_GET
def banner(request):
  banners = Banner.objects.all()
  data = [
    {
      "id": banner.id,
      "title": banner.title,
      "description": banner.description,
      "image": banner.image.url if banner.image else None,
    }
    for banner in banners
  ]

  return JsonResponse({'banner': data}, safe=False)


@require_GET
def sellers(request):
  seller = Sellers.objects.all()

  data = [
    {
      'id': s.id,
      'name': s.name,
      'description': s.description,
      'contacts': s.contacts,
      'price': s.price,
      'logo': s.logo.url if s.logo else None,
    }
    for s in seller
  ]

  return JsonResponse({'seller': data}, safe=False)