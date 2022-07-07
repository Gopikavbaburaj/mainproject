from django.urls import path

from Rewrd_Management_App import employee_views
from Rewrd_Management_App.employee_views import IndexView, Blockchain_admin_Login, View_coupon, view_ledger_login, \
    view_block_chain, Profile_view

urlpatterns = [

    path('',IndexView.as_view()),
    path('admin_login',Blockchain_admin_Login.as_view()),
    path('View_coupon',View_coupon.as_view()),
    path('view_ledger_login', view_ledger_login.as_view()),
    path('get_chain', employee_views.get_chain, name="get_chain"),
    # path('mine_block', user_views.mine_block,name="mine_block"),
    path('is_valid', employee_views.is_valid, name="is_valid"),

    path('view_block_chain', view_block_chain.as_view()),
    path('profile',Profile_view.as_view())

]
def urls():
    return urlpatterns, 'employee', 'employee'