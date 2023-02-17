from django.shortcuts import render
import json
from django.http import JsonResponse
# Create your views here.

def api_home(request):

    body = request.body #Byte string for json data
    print(request.GET)
    print(request.POST)
    data ={}
    try:
        data = json.loads(body) #-->converts json to python dict
    except:
        pass

    print(json.dumps(dict(request.headers)))
    # data['header'] = request.headers #  this was not JSON serializable because JsonResponse couldn't convert it  to json again
    data['header'] = json.dumps(dict(request.headers)) # This is the solution for the above.
    data['content_type']= request.content_type
    print(data)
    return  JsonResponse(data)