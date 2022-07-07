from django.urls import path

from Rewrd_Management_App.customer_views import IndexView, Singleproducts, Add_cart, View_Cart, payment, RejectcartView, \
    Chpayment, Delete_product, Reward_radeem

urlpatterns = [

    path('',IndexView.as_view()),
    path('single',Singleproducts.as_view()),
    path('Add_cart',Add_cart.as_view()),
    path('View_Cart',View_Cart.as_view()),
    path('payment',payment.as_view()),
    path('reject',RejectcartView.as_view()),
    path('Chpayment',Chpayment.as_view()),
    path('delete',Delete_product.as_view()),
    path('Reward_radeem',Reward_radeem.as_view())


]
def urls():
    return urlpatterns, 'customer', 'customer'