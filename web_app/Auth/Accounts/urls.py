from django.urls import path
from . import views
from .views import MyTokenObtainPairView
# ----------------------------------------------------------------
from .views import signup, ProductCountView, ShelfProductList, ZoneProductList, BuyerOrderList, SupplierOrderList, OrderCountView, ProductByClassificationView, ListClassification, DetailClassification, ClassificationUpdateView, ClassificationDeleteView, ListZone, DetailZone, ZoneUpdateView, ZoneDeleteView, ZoneCountView, ListSupplier, DetailSupplier, SupplierUpdateView, SupplierDeleteView, ListBuyer, DetailBuyer, BuyerUpdateView, BuyerDeleteView, ListSeason, DetailSeason, SeasonUpdateView, SeasonDeleteView, ListCarDrop, DetailCarDrop, CarDropUpdateView, CarDropDeleteView, ListShelf, DetailShelf, ShelfDeleteView, ShelfUpdateView, ListProduct, DetailProduct, ProductUpdateView, ProductDeleteView, ListOrder, DetailOrder, OrderUpdateView, OrderDeleteView, ListUser, DetailUser
# ----------------------------------------------------------------


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),
    # ----------------------------------------------------------------------------------

    path('Signin/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', signup, name='signup'),




    # ----------------------------------------------------------------
    path('Classification/', ListClassification.as_view(), name='categorie'),
    path('Classification/<int:pk>/', DetailClassification.as_view(),
         name='singleClassification'),
    path('Classification/<int:pk>/delete/',
         ClassificationDeleteView.as_view(), name='Classification'),
    path('Classification/<int:id>/update/',
         ClassificationUpdateView.as_view(), name='update_Classification'),

    path('classification/<int:classification_id>/products/',
         ProductByClassificationView.as_view(), name='product-by-classification'),




    path('Zone/', ListZone.as_view(), name='Zone'),
    path('Zone/<int:pk>/', DetailZone.as_view(), name='singleZone'),
    path('Zone/<int:pk>/delete/', ZoneDeleteView.as_view(), name='deleteZone'),
    path('Zone/<int:id>/update/', ZoneUpdateView.as_view(), name='update_Zone'),
    path('Zone-count/', ZoneCountView.as_view(), name='zone-count'),

    path('zone-producs/<int:zone_id>/',
         ZoneProductList.as_view(), name='zone-producs'),


    path('Supplier/', ListSupplier.as_view(), name='Supplier'),
    path('Supplier/<int:pk>/', DetailSupplier.as_view(), name='singleSupplier'),
    path('Supplier/<int:pk>/delete/',
         SupplierDeleteView.as_view(), name='Supplier'),
    path('Supplier/<int:id>/update/',
         SupplierUpdateView.as_view(), name='update_Supplier'),

    path('supplier-products/<int:supplier_id>/',
         SupplierOrderList.as_view(), name='supplier_product'),


    path('Buyer/', ListBuyer.as_view(), name='Buyer'),
    path('Buyer/<int:pk>/', DetailBuyer.as_view(), name='singleBuyer'),
    path('Buyer/<int:pk>/delete/', BuyerDeleteView.as_view(), name='Buyer'),
    path('Buyer/<int:id>/update/', BuyerUpdateView.as_view(), name='update_Buyer'),

    path('buyer-orders/<int:buyer_id>/',
         BuyerOrderList.as_view(), name='buyer_orders'),



    path('Season/', ListSeason.as_view(), name='Season'),
    path('Season/<int:pk>/', DetailSeason.as_view(), name='singleSeason'),
    path('Season/<int:pk>/delete/', SeasonDeleteView.as_view(), name='Season'),
    path('Season/<int:id>/update/',
         SeasonUpdateView.as_view(), name='update_Season'),

    path('CarDrop/', ListCarDrop.as_view(), name='CarDrop'),
    path('CarDrop/<int:pk>/', DetailCarDrop.as_view(), name='singleCarDrop'),
    path('CarDrop/<int:pk>/delete/', CarDropDeleteView.as_view(), name='CarDrop'),
    path('CarDrop/<int:id>/update/',
         CarDropUpdateView.as_view(), name='update_CarDrop'),


    path('Shelf/', ListShelf.as_view(), name='Shelf'),
    path('Shelf/<int:pk>/', DetailShelf.as_view(), name='singleShelf'),
    path('Shelf/<int:pk>/delete/', ShelfDeleteView.as_view(), name='deleteShelf'),
    path('Shelf/<int:id>/update/', ShelfUpdateView.as_view(), name='update_Shelf'),


    path('shelf-producs/<int:shelf_id>/',
         ShelfProductList.as_view(), name='shelf-producs'),

    path('Product/', ListProduct.as_view(), name='Product'),
    path('Product/<int:pk>/', DetailProduct.as_view(), name='singleProduct'),
    path('Product/<int:pk>/delete/',
         ProductDeleteView.as_view(), name='deleteProduct'),
    path('Product/<int:id>/update/',
         ProductUpdateView.as_view(), name='update_Product'),
    path('product-count/', ProductCountView.as_view(), name='product-count'),


    path('Order/', ListOrder.as_view(), name='Order'),
    path('Order/<int:pk>/', DetailOrder.as_view(), name='singleOrder'),
    path('Order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
    path('Order/<int:id>/update/', OrderUpdateView.as_view(), name='update_Order'),
    path('order-count/', OrderCountView.as_view(), name='product-count'),





    # path('Delivery/', ListDelivery.as_view(), name='Delivery'),
    # path('Delivery/<int:pk>/', DetailDelivery.as_view(), name='singleDelivery'),
    # path('Delivery/delete/<int:pk>/', DeleteDelivery.as_view(), name='delivery-delete'),
    # path('Delivery/<int:id>/update/', DeliveryUpdateView.as_view(), name='update_Delivery'),
    # path('Delivery-count/', DeliveryCountView.as_view(), name='delivery-count'),



    path('users/', ListUser.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),

]
