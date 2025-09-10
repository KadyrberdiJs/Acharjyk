from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from main.models import Banner


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
