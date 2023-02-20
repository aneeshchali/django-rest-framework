from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict


##Django rest frameowrk responsr is shown below:
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import  api_view
# Create your views here.
from products.models import Product

@api_view(["GET"])
def api_home(request):
    """

    :param normal request:
    :return: returning model imple property data:
    """
    instance = Product.objects.all().order_by('?').first() # random query set from ?
    data = {}

    if instance:
        # data = model_to_dict(model_data,fields=['id','title','price','content'])
        data =  ProductSerializer(instance).data
        print(data)
        return  Response(data)
            #default content_type of httpResponse is text/str
    # return  HttpResponse(data,headers={'content-type':'application/json'})