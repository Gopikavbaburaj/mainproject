from django.urls import path

from Rewrd_Management_App.admin_views import IndexView, Addproduct, Coupon_Category, Coupon_Details, View_product, \
    Shop_Approvel, ApproveView, RejectView, Employee_Approvel, View_employee, Profile_details

urlpatterns = [

    path('',IndexView.as_view()),

    path('shop_approval',Shop_Approvel.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('Employee_Approvel',Employee_Approvel.as_view()),
    path('View_employee',View_employee.as_view()),
    path('single_view',Profile_details.as_view())


]
def urls():
    return urlpatterns, 'admin','admin'