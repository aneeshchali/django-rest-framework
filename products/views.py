from rest_framework import generics, mixins, viewsets, views,permissions,authentication
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffPermission
from api.authentication import TokenAuthentication


class ProductManageAllView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    #This permission classes can be added in tbesettings of the django main app
    permission_classes = [permissions.IsAdminUser,IsStaffPermission]

    def get(self,request,*args,**kwargs):

        pk = kwargs.get('pk')

        if pk == None:
            return self.list(request,**kwargs)
        return self.retrieve(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset()
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        return  qs.filter(user=request.user)

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        None
        #better way is done in the serializer class just using the source.
        if content is None:
            content = title
        serializer.save(content=content,title=title.capitalize())


    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    #also encompasses the perform update method in it.


    def delete(self,request,*args,**kwargs):
        return  self.destroy(request,*args,**kwargs)









#
# class ProductCreateView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def perform_create(self, serializer):
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         None
#         if content is None:
#             content = title
#         serializer.save(content=content)
#
#
# #minor difference than the retrieve generc as it fetches all the value in the database and lists them
# #while on the other hand the data in the Retrieve is basically used to fetch the partiular field
# class ProductListApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
#
# class ProductUpdateApiView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'
#
#     def perform_update(self, serializer):
#         instance = serializer.save()
#         if not instance.content:
#             instance.content = instance.title
#
#
#
# class ProductDeleteApiView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'
#
#     def perform_destroy(self, instance):
#         super().perform_destroy(instance)
#
#
#
# class ProductDetailApiView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# lookup_field = 'pk' find the object accordingly
