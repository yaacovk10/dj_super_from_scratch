from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from base.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET'])
def index(req):
    return Response("test")

@api_view(['GET','POST','DELETE','PUT','PATCH'])
def products(req,id=-1):
    print(req.data)
    print(id)
    if req.method =='GET':
        if id > -1:
            try:
                temp_prod=Product.objects.get(id=id)
                return Response (ProductSerializer(temp_prod,many=True).data)
            except Product.DoesNotExist:
                return Response ("not found")
        all_tasks=ProductSerializer(Product.objects.all(),many=True).data
        return Response (all_tasks)
    if req.method =='POST':
        prod_serializer = ProductSerializer(data=req.data)
        if prod_serializer.is_valid():
            prod_serializer.save()
            return Response (f"product {req.data} added ")
        else:
            return Response (prod_serializer.errors)
    # TODO : how to send id param
    if req.method =='DELETE':
        try:
            temp_prod=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response ("not found")    
       
        temp_prod.delete()
        return Response (f"{req.data} deleted")
    # TODO : how to send id param
    if req.method =='PUT':
        print(f"id {id}")
        try:
            temp_prod=Product.objects.get(id=id)
        except Product.DoesNotExist:
            print("i'm in put")
            print(f"id : {id}")
            print(f"type of id  {type(id)}")
            return Response ("not found")
       
        ser = ProductSerializer(data=req.data)
        old_prod = Product.objects.get(id=id)
        res = ser.update(old_prod, req.data)
        return Response(res)



class Category_view(APIView):
    def get(self, request):
        my_model = Category.objects.all()
        serializer = CategorySerializer(my_model, many=True)
        return Response(serializer.data)
    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = CategorySerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Category.objects.get(pk=pk)
        serializer = CategorySerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Category.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["post"])
def register(req):
    User.objects.create_user(username=req.data["username"],password=req.data["password"])
    return Response( {"user_created":req.data["username"]})


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom columns (user return payload - when login )
        token['username'] = user.username
        token['emaillll'] = user.email
        token['blabla'] = "waga baga bbb"
        # ...
        return token




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
#structure for cart function
def member_only(req):
    return Response ( {"secret":f"you are {req.user}"})