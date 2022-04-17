from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from djangoApi import views

router = DefaultRouter()

router.register('products-api', views.ProductAPI, basename='Product-API')
router.register('operation-api', views.OperationAPI, basename='Operation-API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('operation-filter', views.OperationFilterAPI.as_view()),
    path('', include(router.urls))
]
