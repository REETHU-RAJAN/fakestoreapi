from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import UserSerializer,CategorySerializer,ProductSerializer
from rest_framework.viewsets import ModelViewSet,ViewSet
from store.models import Category,User,Products
from rest_framework.decorators import action
from rest_framework import authentication
from rest_framework import permissions
# Create your views here.
 
class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializers=UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        else:
            return Response(data=serializers.errors)
        
class CategoryView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CategorySerializer
    model=Category
    queryset=Category.objects.all()

    @action(methods=["post"],detail=True)
    def add_products(self,request,*args,**kwargs):
        vid=kwargs.get("pk")
        varient_obj=Category.objects.get(id=vid)
       
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=varient_obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ProductView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProductSerializer
    model=Products
    queryset=Products.objects.all()