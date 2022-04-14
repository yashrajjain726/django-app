from django.shortcuts import render
import io

from django.http import HttpResponse
from django.views import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from djangoApi.models import Product
from django.utils.decorators import method_decorator
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ProductAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = ProductSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': "Your data was pushed to the database"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': "Your data was updated on the database"}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        product = Product.objects.get(id=id)
        product.delete()
        msg = {'msg': "Your data was deleted"}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')
