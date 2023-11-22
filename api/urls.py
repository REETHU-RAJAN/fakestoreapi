from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("category",views.CategoryView,basename="category")



urlpatterns = [

]+router.urls
