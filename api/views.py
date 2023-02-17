from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from products.models import Product

@api_view(["GET"])
def api_home(request):
    """

    :param practice model:
    :return: whole model
    """


    model_data = Product.objects.all().order_by('?').first() # random query set from ?
    data = {}

    if model_data:
        data = model_to_dict(model_data,fields=['id','title','price','content'])
            #default content_type of httpResponse is text/str
    return  Response(data)