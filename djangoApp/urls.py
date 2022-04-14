from django.contrib import admin
from django.urls import path, include
from djangoApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('products-api/', views.ProductAPI.as_view()),
    path('product-api/<int:id>/', views.ProductAPI.as_view()),
    path('operation-api/', views.OperationAPI.as_view()),
    path('operation-api/<int:id>/', views.OperationAPI.as_view()),
    path('operation/filter', views.OperationFilterAPI.as_view())
]
