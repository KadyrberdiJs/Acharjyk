from django.contrib import admin

from main.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
  list_display = ('title', 'short_description', 'created_at',)
  search_fields = ('title', 'description',)
  readonly_fields = ('created_at',)
  
  fieldsets = (
      ('Achar information', {
          "fields": ('title', 'description', 'image', 'created_at',),
      }),
  )

  def short_description(self, obj):
      return (obj.description[:50]+ '...') if len(obj.description) > 50 else obj.description
  
  short_description.short_description = "Description"