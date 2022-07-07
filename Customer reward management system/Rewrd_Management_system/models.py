
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class Customer_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=100, null=True)
    phonenumber=models.CharField(max_length=50, null=True)
    con_password = models.CharField(max_length=50, null=True)

class Shop_Registration(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   phonenumber = models.CharField(max_length=100,null=True)
   address = models.CharField(max_length=100,null=True)

class Product(models.Model):
    name=models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='media/', null=True)
    desc=models.TextField(null=True)
    price=models.IntegerField(null=True)
    shop = models.ForeignKey(Shop_Registration, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    payment = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    delivery = models.CharField(max_length=100,null=True)

class Coupon_Catg(models.Model):
    name=models.CharField(max_length=200)

class Coupon(models.Model):
    code=models.CharField(max_length=50,unique=True)
    discount=models.IntegerField(null=True)
    startvalue=models.IntegerField(null=True)
    endvalue=models.IntegerField(null=True)

    status = models.CharField(max_length=200, null=True)
    blockchain_status = models.CharField(max_length=100, default='not active')
    blockchain_count = models.IntegerField(default=0)
    blockchain_entry_count = models.IntegerField(default=0)
    catg=models.ForeignKey(Coupon_Catg,on_delete=models.CASCADE,null=True)
    shop = models.ForeignKey(Shop_Registration, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)





class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200,null=True)
    phonenumber=models.CharField(max_length=50,unique=True,null=True)
    department = models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=50,null=True)
    shop = models.ForeignKey(Shop_Registration, on_delete=models.CASCADE,null=True)




class Blockchain_admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200,null=True)
    designation = models.CharField(max_length=200, null=True)
    status=models.CharField(max_length=200,null=True)
    key=models.CharField(max_length=200,null=True)
    key2=models.CharField(max_length=200,null=True,default="null")


class blockchain_ledger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE,null=True)

    date = models.DateField(null=False, blank=False, auto_now=True)
    time = models.DateTimeField(max_length=100, auto_now=True)
    Remark = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    blockchain_count = models.IntegerField(default=0)
    blockchain_entry_count = models.IntegerField(default=0)
    last_status = models.CharField(max_length=100,default='not active')

    remarks = models.CharField(max_length=200, null=True)
    count = models.IntegerField(null=True)


class Cart_Total(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    total = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True)


class Blockchain_ledger_encripted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=100, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(auto_now=True)
    Remark = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    blockchain_count = models.CharField(max_length=100,default=0)
    blockchain_entry_count = models.CharField(max_length=100,default=0)
    last_status = models.CharField(max_length=100, default='not active')
    remarks = models.CharField(max_length=200, null=True)
    count = models.IntegerField(null=True)