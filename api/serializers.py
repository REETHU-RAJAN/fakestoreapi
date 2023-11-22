from rest_framework import serializers

from store.models import Category

class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    is_active=serializers.CharField(read_only=True)
    class Meta:
        model=Category
        fields="__all__"