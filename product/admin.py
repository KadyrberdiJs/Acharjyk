from django.contrib import admin

from product.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
  search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}
  list_display = ('name', 'category', 'downloads', 'created_at')
  list_filter = ('category',)
  search_fields = ('name', 'creater', 'category',)
  readonly_fields = ('downloads',)

  fieldsets = (
      ('Achar information', {
          "fields": ('name', 'slug', 'creater', 'category', 'price', 'file',),
      }),
      ('Details', {
        "fields": ('downloads',)
      })
  )


