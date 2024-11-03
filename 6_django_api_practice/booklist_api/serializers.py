from rest_framework import serializers
from .models import Book, Category
from decimal import Decimal

# relationship serializers
# Method 1: create a related serializer
class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']


class BookSerializer(serializers.ModelSerializer):
    # change output name "title" to "name"
    name = serializers.CharField(source="title")
    # calculate in serializers
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')

    # relationship serializers
    # Method 1: create a related serializer
    category = CategorySerializer(read_only=True)

    # Deserializers
    # add additional write_only variable for POST
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Book
        fields = ["id","name","author","price","price_after_tax", "category", "category_id"]
        # relationship serializers
        # Method 2: add depth
        # depth = 1

    def calculate_tax(self, product:Book):
        return round(product.price * Decimal(1.1), 2)
    
