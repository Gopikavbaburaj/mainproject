from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from Rewrd_Management_App.models import Product, Cart, Coupon, Cart_Total, Customer_Reg


class IndexView(TemplateView):
    template_name = 'customer/product_view.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        view_pp = Product.objects.all()
        context['view_pp'] = view_pp
        return context


class Singleproducts(TemplateView):
    template_name = 'customer/single_view.html'
    def get_context_data(self, **kwargs):
        id = self.request.GET['id']

        context = super(Singleproducts, self).get_context_data(**kwargs)

        single_view = Product.objects.get(id=id)

        context['single_view'] = single_view

        return context

class Add_cart(TemplateView):
    template_name = 'customer/single_view.html'
    def dispatch(self,request,*args,**kwargs):
        pid = request.GET['id']
        ca = Cart()
        ca.user = User.objects.get(id=self.request.user.id)
        ca.product = Product.objects.get(pk=pid)
        ca.payment = 'null'
        ca.status = 'cart'
        ca.delivery = 'null'
        ca.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"cart"})






class View_Cart(TemplateView):
    template_name = 'customer/cart.html'


    def get_context_data(self, **kwargs):

        context = super(View_Cart, self).get_context_data(**kwargs)
        cr = self.request.user.id
        ct = Cart.objects.filter(status='cart', user_id=cr, delivery='null')
        cou = Coupon.objects.filter(blockchain_status='active')


        total = 0
        for i in ct:

            total = total + int(i.product.price)


        context['cou'] = cou
        context['ct'] = ct
        context['asz'] = total

        return context



class Reward_radeem(TemplateView):
    template_name = 'customer/cart.html'





class Delete_product(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Product.objects.get(id=id).delete()

        return render(request,'shop/View_product.html',{'message':"Photo Removed"})


class RejectcartView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Cart.objects.get(id=id).delete()

        return redirect(request.META['HTTP_REFERER'])

class Chpayment(TemplateView):
    template_name = 'customer/check-out.html'
    def get_context_data(self, **kwargs):
         context = super(Chpayment,self).get_context_data(**kwargs)
         user = User.objects.get(pk=self.request.user.id)
         id = self.request.GET['id']


         coutomer = Customer_Reg.objects.get(user_id=self.request.user.id)

         cr = self.request.user.id
         ct = Cart.objects.filter(status='cart',user_id=cr)
         cou = Coupon.objects.filter(blockchain_status='active')
         ca = Cart_Total()
         ca.total = id
         ca.user = user
         ca.status = 'notpaid'
         ca.save()
         total=0
         for i in ct:
          total = total + int(i.product.price)
         print(total)

         context['ct'] = ct
         context['coutomer']=coutomer
         context['asz'] = total
         context['cou']=cou

         context['s']=ca.id

         return context
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        coupon=request.POST['coupon']
        id=request.POST['id']
        print("nnnnnnnnnnnnnnnnnnnnnn",id)
        total=request.POST['total']
        print("1111111111111",total)
        print(coupon,'hgcghv')
        print(coupon, 'hgcghv')
        cou=Coupon.objects.get(id=coupon)
        print(cou.startvalue)
        discount=cou.discount

        startvalue=cou.startvalue
        endvalue=cou.endvalue
        print("222222222222")
        if Cart_Total.objects.get(user_id=user.id,status="notpaid"):
            print("99999999")
            if ((int(total)>=int(startvalue)) and (int(total)<int(endvalue))):
                con=Cart_Total.objects.get(id=id)
                print("5555555555555555555555555555555")
                discountamt=int(total)-(discount)
                con.coupon_id=coupon
                con.total=discountamt
                con.status='paid'
                con.save()

                print(discountamt,"divscvvabbsbsbb")
                return render(request, 'customer/payment.html',{'message':" coupon added ",'total':discountamt})
            else:

                con=Cart_Total.objects.get(id=id)
                con.status='paid'
                con.save()



                return render(request, 'customer/payment.html', {'message': " coupon not  valid",'total':total})


        else:
            return render(request, 'customer/check-out.html', {'message': " error"})

class checkout(TemplateView):
    template_name = 'customer/chechout.html'




class payment(TemplateView):
    def dispatch(self,request,*args,**kwargs):

        pid = self.request.user.id


        ch = Cart.objects.filter(user_id=pid,status='cart')


        print(ch)
        for i in ch:
            i.payment='paid'
            i.status='paid'
            i.delivery = 'delivered'
            i.billstatus = "null"
            i.save()
        return render(request,'customer/payment.html',{'message':" payment Success"})


