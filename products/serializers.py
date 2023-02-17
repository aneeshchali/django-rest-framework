from django import forms
from rest_framework import  serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    #below code is for name change:
    def get_my_discount(self,obj):
        print(obj.id)
        return obj.get_discount()