from rest_framework import serializers
from api.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='Cat_id.name', read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price', 'Cat_id','category_name')
    
    def to_representation(self, instance):
        # Customize the response to remove Cat_id
        representation = super().to_representation(instance)
        representation.pop('Cat_id')  # Remove Cat_id from the response
        return representation
    

class NestedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price')



class CategorySerializer(serializers.ModelSerializer):
    products = NestedProductSerializer(many=True, read_only=True, source='categoryID')
    class Meta:
        model = Category
        fields = ('id','name','products')
