from rest_framework import serializers
from .models import Banner, Sellers

class BannerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()


    class Meta:
        model = Banner
        fields = ['id', 'title', 'description', 'image', 'created_at']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
    

class SellersSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Sellers
        fields = ['id', 'name', 'description', 'contacts', 'price', 'logo', 'created_at']

    def get_logo(self, obj):
        request = self.context.get('request')
        if obj.logo and request:
            return request.build_absolute_uri(obj.logo.url)
        return None