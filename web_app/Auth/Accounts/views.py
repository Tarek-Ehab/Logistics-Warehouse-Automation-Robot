from django.shortcuts import render

# Create your views here.

# ----------------------------------------

#               Authentication

# ----------------------------------------
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import SignupUserSerializer
# from .models import Note

# ----------------------------------------

#               Warehouse

# ----------------------------------------
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Classification, Zone,Supplier,Buyer,Season,CarDrop,Shelf, Product,Order
from .serializers import RegistrationSerializer,ZoneSerializer,ZoneCountSerializer,OrderCountSerializer,ProductCountSerializer, ClassificationSerializer, SupplierSerializer,BuyerSerializer, SeasonSerializer, CarDropSerializer, ShelfSerializer, ProductSerializer,OrderSerializer, UserSerializer
from .consumers import PracticeConsumer
from rest_framework import status
from rest_framework import serializers
import uuid
from rest_framework.views import APIView





def addbuyer(request):
    return render(request, "addbuyer.html")


def addcarDrop(request):
    return render(request, "addcarDrop.html")


def addclassification(request):
    return render(request, "addclassification.html")


def addorder(request):
    return render(request, "addorder.html")


def addProduct(request):
    return render(request, "addProduct.html")


def addshelf(request):
    return render(request, "addshelf.html")


def addsupplier(request):
    return render(request, "addsupplier.html")


def addZone(request):
    return render(request, "addZone.html")


def buyer(request):
    return render(request, "buyer.html")


def carDrop(request):
    return render(request, "carDrop.html")


def classification(request):
    return render(request, "classification.html")


def dashboard(request):
    return render(request, "dashboard.html")


def index(request):
    return render(request, "index.html")


def order(request):
    return render(request, "order.html")


def productList(request):
    return render(request, "productList.html")


def productsBuyer(request):
    return render(request, "productsBuyer.html")


def productsByClass(request):
    return render(request, "productsByClass.html")


def ProductsBySupplier(request):
    return render(request, "ProductsBySupplier.html")


def productsZone(request):
    return render(request, "productsZone.html")


def shelf(request):
    return render(request, "shelf.html")


def supplier(request):
    return render(request, "supplier.html")


def updatebuyer(request):
    return render(request, "updatebuyer.html")


def updatecardrop(request):
    return render(request, "updatecardrop.html")


def updateclassification(request):
    return render(request, "updateclassification.html")


def updatedelivery(request):
    return render(request, "updatedelivery.html")


def updateorder(request):
    return render(request, "updateorder.html")


def updateproduct(request):
    return render(request, "updateproduct.html")


def updateshelf(request):
    return render(request, "updateshelf.html")


def updatesupplier(request):
    return render(request, "updatesupplier.html")


def updateZone(request):
    return render(request, "updateZone.html")


def user(request):
    return render(request, "user.html")


def zone(request):
    return render(request, "zone.html")


# -------------------------------


# ---------------------------------------------------------------
# ------------------------Authentication-------------------------
# ---------------------------------------------------------------


class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializers.errors}, status=status.HTTP_404_NOT_FOUND)


        

# -----------------------------------------------------------------------


@api_view(['POST'])
def signup(request):
    serializer = SignupUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# ------------------------------------------------------------------------


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['email'] = user.email
#         token['username'] = user.username
#         return token

#     def validate(self, attrs):
#         username = attrs.get("username")
#         email = attrs.get("email")
#         password = attrs.get("password")

#         if email and password and username:
#             user = authenticate(email=email, password=password,username=username)
#             if not user:
#                 raise serializers.ValidationError("Invalid email or password.")
#         else:
#             raise serializers.ValidationError("Email and password are required.")
# #         data = super().validate(attrs)
# #         refresh = self.get_token(self.user)
# #         data['refresh'] = str(refresh)
# #         data['access'] = str(refresh.access_token)
# #         return data

#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['refresh'] = str(refresh)
#         data['Token'] = str(refresh.access_token)
#         return data

# ------------------------------------------------------

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer





# ----------------------------------------------------------------
# ------------------------Ware House----------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

class ListClassification(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Classification Already Exist.'},status=status.HTTP_404_NOT_FOUND)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DetailClassification(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer



class ClassificationUpdateView(generics.UpdateAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        classification_id = kwargs.get('id')
        classification = self.get_object()
        serializer = self.get_serializer(classification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "message": "Classification updated successfully.","data": serializer.data})

            # return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    
class ClassificationDeleteView(APIView):
    def delete(self, request, pk):
        try:
            classification = Classification.objects.get(pk=pk)
        except Classification.DoesNotExist:
            return Response({"message": "Classification not found."}, status=status.HTTP_404_NOT_FOUND)

        classification.delete()
        return Response({"message": "Classification deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class ProductByClassificationView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        classification_id = self.kwargs['classification_id']
        return Product.objects.filter(classification_id=classification_id)

class BuyerOrderList(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        buyer_id = self.kwargs['buyer_id']
        return Order.objects.filter(buyer__id=buyer_id)



class SupplierOrderList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        supplier_id = self.kwargs['supplier_id']
        return Product.objects.filter(supplier_id=supplier_id)




class ListSupplier(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Supplier Already Exist.'},status=status.HTTP_404_NOT_FOUND)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class DetailSupplier(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierUpdateView(generics.UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        supplier_id = kwargs.get('id')
        supplier = self.get_object()
        serializer = self.get_serializer(supplier, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# class DeleteSupplier(generics.DestroyAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
    
class SupplierDeleteView(APIView):
    def delete(self, request, pk):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({"message": "Supplier not found."}, status=status.HTTP_404_NOT_FOUND)

        supplier.delete()
        return Response({"message": "Supplier deleted successfully."}, status=status.HTTP_204_NO_CONTENT)





class ListBuyer(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Buyer Already Exist.'},status=status.HTTP_404_NOT_FOUND)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class DetailBuyer(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    

# class DeleteBuyer(generics.DestroyAPIView):
#     queryset = Buyer.objects.all()
#     serializer_class = BuyerSerializer
    
class BuyerDeleteView(APIView):
    def delete(self, request, pk):
        try:
            buyer = Buyer.objects.get(pk=pk)
        except Buyer.DoesNotExist:
            return Response({"message": "Buyer not found."}, status=status.HTTP_404_NOT_FOUND)

        buyer.delete()
        return Response({"message": "Buyer deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class BuyerUpdateView(generics.UpdateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        buyer_id = kwargs.get('id')
        buyer = self.get_object()
        serializer = self.get_serializer(buyer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)





# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------

class ListZone(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Zone Already Exist.'},status=status.HTTP_404_NOT_FOUND)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DetailZone(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer



class ZoneUpdateView(generics.UpdateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        zone_id = kwargs.get('id')
        zone = self.get_object()
        serializer = self.get_serializer(zone, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ "message": "Zone updated successfully.","data": serializer.data})

            # return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    
class ZoneDeleteView(APIView):
    def delete(self, request, pk):
        try:
            zone = Zone.objects.get(pk=pk)
        except Zone.DoesNotExist:
            return Response({"message": "Zone not found."}, status=status.HTTP_404_NOT_FOUND)

        zone.delete()
        return Response({"message": "Zone deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class ZoneCountView(APIView):
    def get(self, request):
        count = Zone.objects.count()
        serializer = ZoneCountSerializer({'count': count})
        return Response(serializer.data)


class ZoneProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        zone_id = self.kwargs['zone_id']
        return Product.objects.filter(zone_id=zone_id)


# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------




    
class ListSeason(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Season Already Exist.'},status=status.HTTP_404_NOT_FOUND)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@permission_classes([IsAuthenticated])
class DetailSeason(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    

# class DeleteSeason(generics.DestroyAPIView):
#     queryset = Season.objects.all()
#     serializer_class = SeasonSerializer
    
    

class SeasonUpdateView(generics.UpdateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        season_id = kwargs.get('id')
        season = self.get_object()
        serializer = self.get_serializer(season, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



class SeasonDeleteView(APIView):
    def delete(self, request, pk):
        try:
            season = Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            return Response({"message": "Season not found."}, status=status.HTTP_404_NOT_FOUND)

        season.delete()
        return Response({"message": "Season deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class ListCarDrop(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = CarDrop.objects.all()
    serializer_class = CarDropSerializer


    def create(self, request, *args, **kwargs):
        print(request.data)
        model,is_careted = CarDrop.objects.get_or_create(drop_name=request.data.get('drop_name',None))
        if not is_careted:    
            return Response({'massage':"exist"}, status=status.HTTP_200_OK)
        serializer = self.serializer_class(model)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DetailCarDrop(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = CarDrop.objects.all()
    serializer_class = CarDropSerializer



class CarDropUpdateView(generics.UpdateAPIView):
    queryset = CarDrop.objects.all()
    serializer_class = CarDropSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        cardrop_id = kwargs.get('id')
        cardrop = self.get_object()
        serializer = self.get_serializer(cardrop, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# class DeleteCarDrop(generics.DestroyAPIView):
#     queryset = CarDrop.objects.all()
#     serializer_class = CarDropSerializer
    
class CarDropDeleteView(APIView):
    def delete(self, request, pk):
        try:
            cardrop = CarDrop.objects.get(pk=pk)
        except CarDrop.DoesNotExist:
            return Response({"message": "CarDrop not found."}, status=status.HTTP_404_NOT_FOUND)

        cardrop.delete()
        return Response({"message": "CarDrop deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



class ListShelf(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'message': 'Shelf Already Exist.'},status=status.HTTP_404_NOT_FOUND)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DetailShelf(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    


class ShelfUpdateView(generics.UpdateAPIView):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        shelf_id = kwargs.get('id')
        shelf = self.get_object()
        serializer = self.get_serializer(shelf, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# class DeleteShelf(generics.DestroyAPIView):
#     queryset = Shelf.objects.all()
#     serializer_class = ShelfSerializer
    
class ShelfDeleteView(APIView):
    def delete(self, request, pk):
        try:
            shelf = Shelf.objects.get(pk=pk)
        except Shelf.DoesNotExist:
            return Response({"message": "Shelf not found."}, status=status.HTTP_404_NOT_FOUND)

        shelf.delete()
        return Response({"message": "Shelf deleted successfully."}, status=status.HTTP_204_NO_CONTENT)




class ShelfProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        shelf_id = self.kwargs['shelf_id']
        return Product.objects.filter(shelf_id=shelf_id)



# GET AND POST
# GET AND POST

class ListProduct(generics.ListCreateAPIView):    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        product_name = request.data['name']
        
        try:
            classification = Classification.objects.get(title=request.data['classification'])
        except Classification.DoesNotExist:
            return Response({'message': f"Classification {request.data['classification']} does not exist."}, 
                            status=status.HTTP_404_NOT_FOUND)
        
        
        try:
            supplier = Supplier.objects.get(name=request.data['supplier'])
        except Supplier.DoesNotExist:
            return Response({'message': f"Supplier {request.data['supplier']} does not exist."}, 
                            status=status.HTTP_404_NOT_FOUND)
        

        try:
            shelf = Shelf.objects.get(name=request.data['shelf'])
        except Shelf.DoesNotExist:
            return Response({'message': f"Shelf {request.data['shelf']} does not exist."}, 
                            status=status.HTTP_404_NOT_FOUND)
        
        try:
            zone = Zone.objects.get(name=request.data['zone'])
        except Zone.DoesNotExist:
            return Response({'message': f"Zone {request.data['zone']} does not exist."}, 
                            status=status.HTTP_404_NOT_FOUND)

        # Check if a product with the same name already exists
        if Product.objects.filter(name=product_name).exists():
            return Response({'message': f"A product with the name {product_name} already exists."}, 
                            status=status.HTTP_404_NOT_FOUND)

        qr_code = request.data['qr_code']
        try:
            product = Product.objects.get(qr_code=qr_code)
            return Response({'message': f"The QR code {qr_code} already exists in product {product.name}."}, 
                            status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            pass

        data = request.data.copy()
        data['classification'] = classification.id
        data['supplier'] = Supplier.id
        data['shelf'] = shelf.id
        data['zone'] = zone.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        # Assign the classification and shelf instances to the product object
        product = serializer.save()
        product.classification = classification
        product.supplier = supplier
        product.shelf = shelf
        product.zone = zone
        product.save()
        
          
        # Decrease the shelf capacity by the product quantity
        if shelf.capacity - product.quantity >= 0:
            shelf.capacity -= product.quantity
            shelf.save()
        else:
            # Revert the creation of the product
            product.delete()
            return Response({'message': f"Shelf capacity is not sufficient for this product."}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        
        # Update the product count for the supplier
        supplier.product_count += 1
        supplier.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
    def update(self, request, *args, **kwargs):
        # Get the Product instance to be updated
        product = self.get_object()
        
        # Get the Classification instance and update the product
        classification_title = request.data.get('classification')
        if classification_title:
            try:
                classification = Classification.objects.get(title=classification_title)
            except Classification.DoesNotExist:
                return Response({'error': f'Classification {classification_title} does not exist'}, 
                                status=status.HTTP_404_NOT_FOUND)
            product.classification = classification
        
        
        # Get the supplier instance and update the product
        supplier = request.data.get('supplier')
        if supplier:
            try:
                supplier = Supplier.objects.get(name=supplier)
            except Supplier.DoesNotExist:
                return Response({'error': f'Supplier {supplier} does not exist'}, 
                                status=status.HTTP_404_NOT_FOUND)
            product.supplier = supplier

        # Get the Zone instance and update the product
        zone_name = request.data.get('zone')
        if zone_name:
            try:
                zone = Zone.objects.get(name=zone_name)
            except Zone.DoesNotExist:
                return Response({'error': f'Zone {zone_name} does not exist'}, 
                                status=status.HTTP_404_NOT_FOUND)
            product.zone = zone
            
        
        # Get the Shelf instance and update the product
        shelf_name = request.data.get('shelf')
        if shelf_name:
            try:
                shelf = Shelf.objects.get(name=shelf_name)
            except Shelf.DoesNotExist:
                return Response({'error': f'Shelf {shelf_name} does not exist'}, 
                                status=status.HTTP_404_NOT_FOUND)
            product.shelf = shelf
        
        # Update the product using the serializer
        serializer = self.get_serializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)

# class DeleteProduct(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
class ProductDeleteView(APIView):
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        
        supplier = product.supplier
        supplier.product_count -= 1
        supplier.save()

        product.delete()
        return Response({"message": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


    
class ProductCountView(APIView):
    def get(self, request):
        count = Product.objects.count()
        serializer = ProductCountSerializer({'count': count})
        return Response(serializer.data)

class OrderCountView(APIView):
    def get(self, request):
        count = Order.objects.count()
        serializer = OrderCountSerializer({'count': count})
        return Response(serializer.data)
    
class ListOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(name=request.data['product'])
        except Product.DoesNotExist:
            return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

        try:
            buyer = Buyer.objects.get(name=request.data['buyer'])
        except Buyer.DoesNotExist:
            return Response({'message': 'Buyer does not exist'}, status=status.HTTP_404_NOT_FOUND)

        try:
            drop_name = CarDrop.objects.get(drop_name=request.data['drop_name'])
        except CarDrop.DoesNotExist:
            return Response({'message': 'Drop name does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Check if an order already exists for the same product and buyer
        existing_order = Order.objects.filter(product=product, buyer=buyer).first()
        if existing_order:
            return Response({'message': f"An order already exists for product {product.name} and buyer {buyer.name}"}, 
                            status=status.HTTP_409_CONFLICT)

        data = {
            'product': product.id,
            'quantity': request.data['quantity'],
            'buyer': buyer.id,
            'drop_name': drop_name.id,
            'delivery_status': request.data.get('delivery_status')
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        # Check if the quantity of the ordered product is enough
        if int(request.data['quantity']) > product.quantity:
            return Response({'message': f"Not enough quantity for product {product.name}"}, 
                status=status.HTTP_404_NOT_FOUND)

        # Check if the quantity of the ordered product is 0
        elif int(request.data['quantity']) == 0:
            return Response({'message': f"Please specify the quantity for product {product.name}"}, 
                            status=status.HTTP_404_NOT_FOUND)

        # Reduce the quantity of the ordered product
        product.quantity -= int(request.data['quantity'])
        product.save()

        # Create the order
        order = serializer.save()
        order.product = product
        order.buyer = buyer
        order.drop_name = drop_name
        order.save()

        # Update the order count for the buyer
        buyer.order_count += 1
        buyer.save()
        ser_order = OrderSerializer(order)
        print('producton.....')
        PracticeConsumer.send_data(drop_name.drop_name,ser_order.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer




class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = self.get_serializer(order, data=request.data, partial=True)

        # Update product
        product_name = request.data.get('product_name')
        if product_name:
            try:
                product = Product.objects.get(name=product_name)
            except Product.DoesNotExist:
                return Response({'error': f'Product {product_name} does not exist'}, 
                                status=status.HTTP_404_NOT_FOUND)
            order.product = product

        # Update buyer
        buyer_name = request.data.get('buyer_name')
        if buyer_name:
            try:
                buyer = Buyer.objects.get(name=buyer_name)
            except Buyer.DoesNotExist:
                return Response({'error': f'Buyer {buyer_name} does not exist'}, 
                                status=status.HTTP_404_NOT_FOUND)
            order.buyer = buyer

        # Update quantity
        if serializer.is_valid():
            quantity_delta = serializer.validated_data.get('quantity') - order.quantity
            product = order.product
            if order.delivery_status == 'pending':
                quantity = request.data.get('quantity')
                if quantity_delta > 0:
                    if quantity_delta <= product.quantity:
                        product.quantity -= quantity_delta
                        product.save()
                    else :
                        return Response({'message': f"Not enough quantity for product {product.name}"}, status=status.HTTP_404_NOT_FOUND)
                elif quantity_delta < 0:
                    product.quantity += -quantity_delta
                product.save()
                order.quantity = quantity

        # Update season
        season_name = request.data.get('season', {}).get('name')
        if season_name:
            try:
                season = Season.objects.get(name=season_name)
            except Season.DoesNotExist:
                return Response({'error': f'Season {season_name} does not exist'}, 
                                status=status.HTTP_404_NOT_FOUND)
            order.season = season

        # Update order_date
        order_date = request.data.get('order_date')
        if order_date:
            order.order_date = order_date
            
            
        # Update drop_name
        drop_name = request.data.get('drop_name')
        if drop_name:
            try:
                car_drop = CarDrop.objects.get(drop_name=drop_name)
            except CarDrop.DoesNotExist:
                return Response({'error': f'Car drop {drop_name} does not exist'},
                                status=status.HTTP_404_NOT_FOUND)
            order.drop_name = car_drop

        # Update delivery_status
        delivery_status = request.data.get('delivery_status')
        if delivery_status:
            order.delivery_status = delivery_status

        order.save()

        serializer = self.get_serializer(order)
        return Response(serializer.data)

class OrderDeleteView(APIView):
    def delete(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"message": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        buyer = order.buyer
        product = order.product

        if order.delivery_status == 'pending':
            product.quantity += order.quantity
            product.save()

        buyer.order_count -= 1
        buyer.save()

        order.delete()
        return Response({"message": "Order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# class ListOrder(generics.ListCreateAPIView):    
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
  
  

# class OrderUpdateView(generics.UpdateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     lookup_field = 'id'
# # This line defines a method called put that will be called
# # when a PUT request is received by the view.
#     def put(self, request, *args, **kwargs):
# # This line retrieves the id parameter from the URL kwargs dictionary.
#         order_id = kwargs.get('id')
# # This line retrieves the Order instance 
# # that should be updated, based on the id parameter.
#         order = self.get_object()
#         serializer = self.get_serializer(order, data=request.data, partial=True)
#         if serializer.is_valid():
#             old_quantity = order.quantity
#             new_quantity = serializer.validated_data.get('quantity')
#             product = order.product
#             if order.delivery_status == 'pending':
#                 if old_quantity < new_quantity:
#                     product.quantity -= (new_quantity - old_quantity)
#                 elif old_quantity > new_quantity:
#                     product.quantity += (old_quantity - new_quantity)
#                 product.save()
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# class OrderDeleteView(APIView):
#     def delete(self, request, pk):
#         try:
#             order = Order.objects.get(pk=pk)
#         except Order.DoesNotExist:
#             return Response({"message": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

#         # Increase the quantity of the ordered product
#         product = order.product
#         quantity = order.quantity
#         product.quantity += quantity
#         product.save()

#         order.delete()
#         return Response({"message": "order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# class ListDelivery(generics.ListCreateAPIView):
#     queryset = Delivery.objects.all()
#     serializer_class = DeliverySerializer

#     def get(self, request):
#         deliveries = Delivery.objects.all()
#         serializer = DeliverySerializer(deliveries, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         product_name = request.data['order']
#         try:
#             order = Order.objects.get(product__name=product_name)
#         except Order.DoesNotExist:
#             return Response({'message': f"Order with product name {product_name} does not exist."},
#                             status=status.HTTP_404_NOT_FOUND)

#         # Check if a delivery already exists for the order
#         if Delivery.objects.filter(order=order).exists():
#             return Response({'message': f"Delivery already exists for order with product name {product_name}."},
#                             status=status.HTTP_400_BAD_REQUEST)

#         data = request.data.copy()
#         data['order'] = order.id
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)

#         # Assign the order instance to the delivery object
#         delivery = serializer.save(order=order)

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class DetailDelivery(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Delivery.objects.all()
#     serializer_class = DeliverySerializer
# class DeliveryUpdateView(generics.UpdateAPIView):
#     queryset = Delivery.objects.all()
#     serializer_class = DeliverySerializer
#     lookup_field = 'id'

#     def put(self, request, *args, **kwargs):
#         delivery_id = kwargs.get('id')
#         delivery = self.get_object()
#         serializer = self.get_serializer(delivery, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# class DeleteDelivery(generics.DestroyAPIView):
#     queryset = Delivery.objects.all()
#     serializer_class = DeliverySerializer

#     def delete(self, request, *args, **kwargs):
#         delivery = self.get_object()
#         delivery.delete()
#         return Response({"message": "delivery deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# class DeliveryCountView(APIView):
#     def get(self, request):
#         count = Delivery.objects.count()
#         serializer = DeliveryCountSerializer({'count': count})
#         return Response(serializer.data)




# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------





class ListUser(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ----------------------------------------------------------------




@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/Signin',
        '/api/token/refresh',
        '/api/Classification/<int:pk>/',
        'signup/',
    ]

    return Response(routes)
 
 
 

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#     user = request.user
#     notes = user.note_set.all()
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)