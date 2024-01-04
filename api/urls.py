from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("category",views.CategoryView,basename="category")
router.register("products",views.ProductView,basename="products")



urlpatterns = [
    path("register/",views.UserCreationView.as_view()),
    path("token/",ObtainAuthToken.as_view()),

]+router.urls
