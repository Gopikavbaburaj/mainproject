import string
import random

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from Rewrd_Management_App.models import Product, Coupon_Catg, Coupon, Shop_Registration, Employee, Blockchain_admin


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class Shop_Approvel(TemplateView):
    template_name = 'admin/shop_approval.html'

    def get_context_data(self, **kwargs):
        context = super(Shop_Approvel,self).get_context_data(**kwargs)

        shop = Shop_Registration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['shop'] = shop
        return context

class Employee_Approvel(TemplateView):
    template_name = 'admin/employee_approval.html'

    def get_context_data(self, **kwargs):
        context = super(Employee_Approvel,self).get_context_data(**kwargs)

        emp = Employee.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['emp'] = emp
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"cart"})



class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"cart"})


class View_employee(TemplateView):
    template_name = 'admin/view_employe.html'

    def get_context_data(self, **kwargs):
        context = super(View_employee, self).get_context_data(**kwargs)
        emp1 = Employee.objects.filter(user__last_name='1')
        context['emp1'] = emp1
        return context


class Profile_details(TemplateView):
    template_name = 'admin/view_profile.html'

    def get_context_data(self, **kwargs):
        id = self.request.GET['id']

        context = super(Profile_details, self).get_context_data(**kwargs)

        single_view = Employee.objects.get(id=id)

        context['single_view'] = single_view

        return context

    def post(self, request, *args, **kwargs):
        S = 16

        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
        count = len(ran)
        range = ran[0:count:4]
        print(range)
        ascii_values = []
        for i in range:
            print(i)
            ascii_values.append(ord(i))
        values_sum = sum(ascii_values)
        print(values_sum)
        print(ascii_values)
        print("The randomly generated string is : " + str(ran))

        name = request.POST['name']
        desig = request.POST['designation']
        user = request.POST['user']
        dept = request.POST['department']
        employee = request.POST['employee']
        if Blockchain_admin.objects.filter(user_id=user):
            print("fvvfsff")
            return render(request, 'admin/admin_index.html', {'message': "Already Added"})
        else:

            se = Blockchain_admin()
            se.name = name
            se.depatment = dept
            se.designation = desig
            se.user_id = user
            se.employee_id = employee
            se.key = ran
            se.key2=values_sum
            se.status = 'blockchain_admin'

            se.save()

            return render(request, 'admin/admin_index.html', {'message': "Blockchain admin added successfully"})


class Addproduct(TemplateView):
    template_name ='admin/add_product.html'

    def post(self, request,*args,**kwargs):
        user = User.objects.get(pk=self.request.user.id)
        name = request.POST['name']

        price = request.POST['price']
        desc = request.POST['desc']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)

        se = Product()
        se.user=user
        se.name = name
        se.image=filesss
        se.price = price
        se.desc = desc
        se.save()

        return redirect(request.META['HTTP_REFERER'], {'message': "product successfully added "})


class Coupon_Category(TemplateView):
    template_name = 'admin/add_coupon_category.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        categ = Coupon_Catg()
        categ.name = name
        categ.save()
        return redirect(request.META['HTTP_REFERER'], {'message': "Category Successfuly Added"})


class Coupon_Details(TemplateView):
    template_name = 'admin/add_coupon_details.html'


    def get_context_data(self, **kwargs):
        context = super(Coupon_Details, self).get_context_data(**kwargs)
        category = Coupon_Catg.objects.all()
        context['category'] = category
        return context


    def post(self, request,*args,**kwargs):
        code = request.POST['code']
        category = request.POST['category']
        validfrom = request.POST['validfrom']
        validto = request.POST['validto']
        discount=request.POST['discount']

        se = Coupon()
        se.code = code
        se.catg_id = category
        se.valid_from = validfrom
        se.valid_to = validto
        se.discount=discount

        se.save()

        return redirect(request.META['HTTP_REFERER'], {'message': "product successfully added "})


class View_product(TemplateView):
    template_name = 'admin/product_view.html'

    def get_context_data(self, **kwargs):

        context = super(View_product,self).get_context_data(**kwargs)

        view_pr = Product.objects.all()

        context['view_pr'] = view_pr

        return context
