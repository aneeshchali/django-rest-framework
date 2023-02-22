from django import forms
from rest_framework import  serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    #url in the serializer view:
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    class Meta:
        model = Product
        fields = [
            'url',
            'id',
            'title',
            'content',
            'price',
            'sale_price',

            'my_discount',
        ]

    #below code is for name change:
    def get_my_discount(self,obj):

        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return  None
        return obj.get_discount()