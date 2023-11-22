from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from store.models import Category
from api.serializers import CategorySerializer
# Create your views here.

class CategoryView(ModelViewSet):
    serializer_class=CategorySerializer
    model=Category
    queryset=Category.objects.all()
