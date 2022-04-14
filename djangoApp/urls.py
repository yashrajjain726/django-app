from django.contrib import admin
from django.urls import path, include
from djangoApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('productApi/', views.ProductAPI.as_view()),
    path('operation/', views.OperationAPI.as_view())
]
