from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_POST


from product.models import Product

def product_list(request):
  return render(request, "products/product_list.html")

@require_GET
def product(request):
  products = Product.objects.all()

  data = [
    {
      "id": p.id,
      "name": p.name,
      "image": p.image,
      "file": p.request.build_absolute_uri(p.file.url) if p.file else None,
      "downloads": p.downloads,
      "category": p.category.name,
      'image': request.build_absolute_uri(p.image.url) if p.image else None
    }
    for p in products
  ]

  return JsonResponse({'products': data})

@require_POST
def download_product(request, pk):
  product = get_object_or_404(Product, pk)

  # Increase download count 
  product.downloads += 1
  product.save()

  return JsonResponse({
    'success': True,

    'data': {
      "file_url": request.build_absolute_url(product.file.url),
      'downloads': product.downloads
    }
  })