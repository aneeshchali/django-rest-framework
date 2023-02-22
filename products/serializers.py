from django import forms
from rest_framework import  serializers

from .models import Product
from api.serializers import PublicClassSerializers

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    #Below code is used to pass the nested serialized data.
    owner = PublicClassSerializers(source='user',read_only=True)
    #you can make the (write only) field so that the serializers can be user to take iput from the user but not to the model...

    #url in the serializer view:
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            # 'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]


    def validate_title(self,value):
        qs = Product.objects.filter(title__exact=value)
        if qs.exists():
            raise serializers.ValidationError(f'{value} already exist i!')

        return value

        #below code is for name change:
    def get_my_discount(self,obj):

        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return  None
        return obj.get_discount()