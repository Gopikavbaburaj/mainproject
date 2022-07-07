from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from Rewrd_Management_App.models import Customer_Reg, UserType, Shop_Registration



class IndexView(TemplateView):
    template_name = 'index.html'


class Customer_reg(TemplateView):
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        address=request.POST['address']
        phonenumber=request.POST['phonenumber']
        password = request.POST['password']
        con_password = request.POST['con_password']

        # address = request.POST['address']
        if password == con_password:

            if User.objects.filter(email=email):
                print('pass')
                return render(request, 'register.html', {'message': "already added the email"})

            else:
                user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='0')
                user.save()
                customer = Customer_Reg()
                customer.user = user
                customer.address= address
                customer.phonenumber=phonenumber
                customer.con_password=con_password
                customer.save()
                usertype = UserType()

                usertype.user = user
                usertype.type = "customer"
                usertype.save()
                return render(request, 'register.html', {'message': "successfully added"})
        else:
            return render(request, 'register.html', {'message': "password didn't match"})

class Shop_registration(TemplateView):
    template_name = 'shop_registration.html'


    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']

        password = request.POST['password']
        con_password = request.POST['con_password']


        if password == con_password:

            if User.objects.filter(email=email):
                print('pass')
                return render(request, 'index.html', {'message': "already added the username or email"})

            else:
                user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='0')
                user.save()
                shop = Shop_Registration()
                shop.user = user
                shop.phonenumber = phonenumber
                shop.address = address
                shop.con_password = con_password
                # shop.image = files

                shop.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "shop"
                usertype.save()

                return render(request, 'index.html', {'message': "successfully added"})
        else:
            return render(request, 'index.html', {'message': "password didn't match"})

class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "customer":
                    return redirect('/customer')
                elif UserType.objects.get(user_id=user.id).type == "shop":
                    return redirect('/shop')
                elif UserType.objects.get(user_id=user.id).type == "employee":
                    return redirect('/employee')

            else:
                return render(request, 'index.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'index.html', {'message': "Invalid Username or Password"})