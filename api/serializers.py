from rest_framework import serializers

from store.models import Category,Products,User
class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data) 

class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    is_active=serializers.CharField(read_only=True)
    class Meta:
        model=Category
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    category=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Products
        
        fields="__all__"        