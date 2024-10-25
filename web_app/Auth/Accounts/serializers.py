from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Classification, Product,Zone,Supplier,Buyer,Season,CarDrop,Shelf,Order
from django.contrib.auth.models import User


# ---------------------------------------------------------------
# ------------------------Authentication-------------------------
# ---------------------------------------------------------------

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)
  

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


        # --------------------------------------------------
        # ------------NEW SIGNUP POST-----------------------
        # --------------------------------------------------
        
class SignupUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user





# ----------------------------------------------------------------
# ------------------------Ware House----------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------


class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification 
        fields = (
            'id',
            'title',
        )






class SupplierSerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format='%d-%m-%Y',read_only=True)
    product_count = serializers.IntegerField(read_only=True)

    class Meta :
        model = Supplier
        fields = (
        'id', 
        'name',
        'address',
        'phone',
        'email',
        'product_count',
        'created_date',
        )
        
        

class BuyerSerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format='%d-%m-%Y',read_only=True)
    order_count = serializers.IntegerField(read_only=True)

    class Meta :
        model = Buyer
        fields = (
        'id', 
        'name',
        'address',
        'phone',
        'email',
        'order_count',
        'created_date',
        )
 

     
     
    
class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


    
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = (
            'id',
            'name',
        )

        

class CarDropSerializer(serializers.ModelSerializer):
    # season = SeasonSerializer()

    # start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    # end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = CarDrop
        fields = (
            'id', 
            'Car_ID',
            'drop_name', 
            'delivery_status',
            )
        
        
        
class ShelfSerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format='%d-%m-%Y',read_only=True)
    # expiry_date = serializers.DateField(format='%d-%m-%Y',read_only=True)

    class Meta:
        model = Shelf
        fields = (
            'id',
            'name',
            'capacity',
            'created_date',
            'expiry_date',
            )


class SupplierNameSerializer(serializers.ModelSerializer):
    class Meta :
        model = Supplier
        fields = ['name']
        
class ShelfNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ['name']
        
        
class ZoneNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['name']
        
class ClassificationNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification 
        fields = ['title']




class SeasonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['name']



class ProductSerializer(serializers.ModelSerializer):
  classification = ClassificationNameSerializer(read_only=True)
  zone = ZoneNameSerializer(read_only=True)
  shelf = ShelfNameSerializer(read_only=True)
  supplier = SupplierNameSerializer(read_only=True)
  date_created = serializers.DateField(format='%d-%m-%Y',read_only=True)

  class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'supplier',
            'classification',
            'describtion',
            'zone',
            'shelf',
            'price',
            'quantity',
            'qr_code',
            'date_created',
            'status',
        )


class ProductNameSerializer(serializers.ModelSerializer):
    shelf = ShelfNameSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['name','shelf','qr_code']
        
class BuyerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['name']

class SupplierNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name']
        
class SeasonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['name']
        
class CarDropNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDrop
        fields = ['drop_name']
        
        
#product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
#     product_name = serializers.ReadOnlyField(source='product.name')
#     buyer_name = serializers.ReadOnlyField(source='buyer.name')
#     supplier_name = serializers.ReadOnlyField(source='supplier.name')
#     season_name = serializers.ReadOnlyField(source='season.name')
#     drop_namee = serializers.ReadOnlyField(source='drop_name.name')
class ZoneCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()
class ProductCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()
class OrderCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    
class OrderSerializer(serializers.ModelSerializer):
    product = ProductNameSerializer(read_only=True)
    buyer = BuyerNameSerializer(read_only=True)
    drop_name = CarDropNameSerializer(read_only=True)  # update field name to the correct one in your Order model
    class Meta:
        model = Order
        fields = (
            'id',
            'product',
            'buyer',
            'quantity',
            'drop_name',  # update field name to the correct one in your Order model
            'order_date',
            'delivery_status',
        )
        
    # def create(self, validated_data):
    #     # Reduce the quantity of the ordered product
    #     product = validated_data['product']
    #     quantity = validated_data['quantity']
    #     product.quantity -= quantity
    #     product.save()

    #     # Create the order
    #     # so this is equivalent to calling Order.objects.create
    #     # (product=product, quantity=quantity, ...) 
    #     # with all the other fields from validated_data.
    #     order = Order.objects.create(**validated_data)

    #     return order


        
class OrderNameSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    class Meta:
        model = Order
        fields = ['product_name']

# class DeliverySerializer(serializers.ModelSerializer):
#     order_name = OrderNameSerializer(read_only=True, source='order')
#     delivery_date = serializers.DateTimeField(format="%Y-%m-%d Time: %H:%M")
#     class Meta:
#         model = Delivery
#         fields = [
#             'id', 
#             'order_name',
#             'delivery_address', 
#             'delivery_date'
#         ]







class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )

class CartUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')



# ----------------------------------------------------------------


        
        