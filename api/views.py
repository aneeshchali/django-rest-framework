from django.shortcuts import render
import json
from django.http import JsonResponse
# Create your views here.

def api_home(request):

    body = request.body #Byte string for json data
    try:
        data = json.loads(body)
    except:
        pass

    print(data.keys())
    return  JsonResponse({"message":"This is just a message!"})