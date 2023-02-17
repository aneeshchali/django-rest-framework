from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict

# Create your views here.
from products.models import Product

def api_home(request):

    model_data = Product.objects.all().order_by('?').first() # random query set from ?
    data = {}

    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        #model instance (model_data)
        #turn into a py dict
        #return json
#----------------------------------------------------
        #below works same as above in this scenerio.
        data = model_to_dict(model_data,fields=['id','title','price','content'])
        json_data = json.dumps(data)
            #default content_type of httpResponse is text/str
    return  HttpResponse(data,headers={'content-type':'application/json'})