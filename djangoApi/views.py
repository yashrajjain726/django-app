from rest_framework import status
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from djangoApi.models import Product, Operation
from .serializers import ProductSerializer, OperationSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ProductAPI(APIView):
    # GET PRODUCT/PRODUCTS
    def get(self, request, id=None):
        id = id
        if id is not None:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data,)


    # CREATE PRODUCT
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was pushed to the database"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # UPDATE PRODUCT
    def put(self, request, id):
        id = id
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was updated on the database"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE PRODUCT
    def delete(self, request, id):
        id = id
        product = Product.objects.get(id=id)
        product.delete()
        return Response({'msg': "Your data was deleted"})


@method_decorator(csrf_exempt, name='dispatch')
class OperationAPI(APIView):
    # GET OPERATION/OPERATIONS
    def get(self, request, id=None):
        id = id
        if id is not None:
            operation = Operation.objects.get(id=id)
            serializer = OperationSerializer(operation)
            return Response(serializer.data)
        operation = Operation.objects.all()
        serializer = OperationSerializer(operation, many=True)
        return Response(serializer.data,)

    # CREATE OPERATION
    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was pushed to the database"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # UPDATE OPERATION
    def put(self, request, id):
        id = id
        operation= Operation.objects.get(id=id)
        serializer = OperationSerializer(operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was updated on the database"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE OPERATION
    def delete(self, request, id):
        id = id
        operation = Operation.objects.get(id=id)
        operation.delete()
        return Response({'msg': "Your data was deleted"})


@method_decorator(csrf_exempt, name='dispatch')
class OperationFilterAPI(APIView):
    # LIST ALL OPERATIONS
    def get(self, request, *args, **kwargs):
        display_data = Operation.objects.all()
        return render(request, 'index.html', {"data": display_data})

    # LIST ALL OPERATIONS BETWEEN FROM_DATE & TO_DATE
    def post(self, request, *args, **kwargs):
        from_date = request.POST.get('fromdate')
        to_date = request.POST.get('todate')
        search_result = Operation.objects.filter(date__range=[from_date, to_date])
        return render(request, 'index.html', {"data": search_result})
