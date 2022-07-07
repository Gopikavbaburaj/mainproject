from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from Rewrd_Management_App.models import Product, Coupon, Coupon_Catg, Employee, UserType, Blockchain_admin, \
    blockchain_ledger, Shop_Registration


class IndexView(TemplateView):
    template_name = 'shop/shop_index.html'



class Addproduct(TemplateView):
    template_name ='shop/add_product.html'

    def post(self, request,*args,**kwargs):
        user = User.objects.get(pk=self.request.user.id)
        shop = Shop_Registration.objects.get(user_id=self.request.user.id)


        name = request.POST['name']

        price = request.POST['price']
        desc = request.POST['desc']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)

        se = Product()
        se.user=user
        se.shop=shop
        se.name = name
        se.image=filesss
        se.price = price
        se.desc = desc
        se.save()

        return redirect(request.META['HTTP_REFERER'], {'message': "product successfully added "})


class Coupon_Category(TemplateView):
    template_name = 'shop/add_coupon_category.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        categ = Coupon_Catg()
        categ.name = name
        categ.save()
        return redirect(request.META['HTTP_REFERER'], {'message': "Category Successfuly Added"})


class Coupon_Details(TemplateView):
    template_name = 'shop/add_coupon_details.html'





    def post(self, request,*args,**kwargs):
        user = User.objects.get(pk=self.request.user.id)
        shop = Shop_Registration.objects.get(user_id=self.request.user.id)
        code = request.POST['code']

        discount=request.POST['discount']
        startprice=request.POST['startvalue']
        endprice=request.POST['endvalue']


        se = Coupon()
        se.user=user
        se.shop=shop
        se.startvalue=startprice
        se.endvalue=endprice
        se.code = code

        se.discount=discount
        se.status='null'

        se.save()

        return redirect(request.META['HTTP_REFERER'], {'message': "product successfully added "})


class View_product(TemplateView):
    template_name = 'shop/product_view.html'

    def get_context_data(self, **kwargs):

        context = super(View_product,self).get_context_data(**kwargs)

        view_pr = Product.objects.filter(user_id=self.request.user.id)

        context['view_pr'] = view_pr
        return context

class Add_Employee(TemplateView):
    template_name = 'shop/add_employee.html'

    def post(self , request,*args,**kwargs):
        shop = Shop_Registration.objects.get(user_id=self.request.user.id)

        name = request.POST['name']
        designation = request.POST['designation']
        department=request.POST['department']
        address=request.POST['address']
        phonenumber=request.POST['phonenumber']
        email= request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email):
            print ('pass')
            return render(request,'shop/add_employee.html',{'message':"already added the username or email"})

        else:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            emp = Employee()
            emp.user = user
            emp.shop=shop
            emp.designation = designation
            emp.department =department
            emp.phonenumber=phonenumber
            emp.address=address
            emp.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "employee"
            usertype.save()
            return render(request, 'shop/add_employee.html', {'message':"successfully added"})

class View_employee(TemplateView):
    template_name = 'shop/view_employee.html'
    def get_context_data(self, **kwargs):
        id = self.request.user.id
        context = super(View_employee,self).get_context_data(**kwargs)
        shop = Shop_Registration.objects.get(user_id=id)
        emp=shop.id
        feed = Employee.objects.filter(shop_id=emp)

        context['feed'] = feed
        return context

class EmployeeEdit(TemplateView):
    template_name = 'shop/edit_profile.html'

    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        employee = Employee.objects.get(pk=id)
        if request.POST['profile'] == "profile":
            employee.designation=request.POST['designation']
            employee.department = request.POST['department']
            employee.save()
            return render(request,'shop/shop_index.html',{'message':"Employee Profile Updated"})
        else:

            return render(request,'shop/shop_index.html',{'message':" Updated"})