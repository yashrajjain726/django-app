from rest_framework import status, viewsets
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from djangoApi.models import Product, Operation
from .serializers import ProductSerializer, OperationSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ProductAPI(viewsets.ViewSet):

    # GET LIST OF PRODUCTS
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # GET PRODUCT
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            product = Product.objects.get(product_id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

    # CREATE PRODUCT
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was pushed to the database"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # UPDATE PRODUCT
    def update(self, request, pk):
        id = pk
        product = Product.objects.get(product_id=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was updated on the database"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        product = Product.objects.get(product_id=id)
        serializer = ProductSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was updated on the database"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE PRODUCT
    def destroy(self, request, pk):
        id = pk
        product = Product.objects.get(product_id=id)
        product.delete()
        return Response({'msg': "Your data was deleted"})


@method_decorator(csrf_exempt, name='dispatch')
class OperationAPI(viewsets.ViewSet):

    # GET LIST OF OPERATIONS
    def list(self, request):
        operations = Operation.objects.all()
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)

    # GET OPERATION
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            operation = Operation.objects.get(product_id=id)
            serializer = OperationSerializer(operation)
            return Response(serializer.data)

    # CREATE OPERATION
    def create(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was pushed to the database"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # UPDATE OPERATION
    def update(self, request, pk):
        id = pk
        operation = Operation.objects.get(product_id=id)
        serializer = OperationSerializer(operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was updated on the database"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        operation = Operation.objects.get(product_id=id)
        serializer = OperationSerializer(operation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Your data was updated on the database"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE OPERATION
    def destroy(self, request, pk):
        id = pk
        operation = Operation.objects.get(product_id=id)
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
