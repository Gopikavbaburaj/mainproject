from django.urls import path

from Rewrd_Management_App.shop_views import IndexView, Addproduct, Coupon_Category, Coupon_Details, View_product, \
    Add_Employee, View_employee, EmployeeEdit

urlpatterns = [

    path('',IndexView.as_view()),
    path('Addproduct', Addproduct.as_view()),
    path('Coupon_Category', Coupon_Category.as_view()),
    path('Coupon_Details', Coupon_Details.as_view()),
    path('View_product', View_product.as_view()),
    path('Add_Employee',Add_Employee.as_view()),
    path('View_employee',View_employee.as_view()),
    path('employee_edit', EmployeeEdit.as_view())

]

def urls():
    return urlpatterns, 'shop', 'shop'