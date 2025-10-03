from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from rest_framework import generics, status
from django.middleware.csrf import get_token


from product.models import Category, Product
from product.serializer import CategorySerializer, ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_context(self):
        return {'request': self.request}
    

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@require_POST
def  download_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.downloads += 1
    product.save()

    return JsonResponse({
        'success': True,
        'data': {
            'file_url': request.build_absolute_uri(product.file.url),
            'downloads': product.downloads
        }
    })



# @require_GET
# def category(request):
#   category = Category.objects.all()
#   data = [
#     {
#       "id": c.id,
#       "name": c.name,
#       "image": c.image.url if c.image else None
#     }
#     for c in category
#   ]

#   return JsonResponse({'category': data})


# @require_GET
# def product(request):
#   products = Product.objects.all()
#   paginator = Paginator(products, 3)

#   page_number = request.GET.get("page")
#   page_obj = paginator.get_page(page_number)

#   data = [
#     {
#       "id": p.id,
#       "name": p.name,
#       "file": request.build_absolute_uri(p.file.url) if p.file else None,
#       "downloads": p.downloads,
#       "category": p.category.name,
#     }
#     for p in page_obj
#   ]

#   return JsonResponse({'products': data,
#                        'count': paginator.count,
#                        'num_pages': paginator.num_pages,
#                        'current_page': page_obj.number,
#                        })

# @require_POST
# def download_product(request, pk):
#   product = get_object_or_404(Product, pk=pk)

#   # Increase download count 
#   product.downloads += 1
#   product.save()

#   return JsonResponse({
#     'success': True,

#     'data': {
#       "file_url": request.build_absolute_uri(product.file.url),
#       'downloads': product.downloads
#     }
#   })

