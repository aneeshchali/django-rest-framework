from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer



class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        None
        if content is None:
            content = title
        serializer.save(content=content)


#minor difference than the retrieve generc as it fetches all the value in the database and lists them
#while on the other hand the data in the Retrieve is basically used to fetch the partiular field
class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title



class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)



class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' find the object accordingly


