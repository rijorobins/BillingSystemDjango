from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.product_name
class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    purchase_price = models.FloatField(null=False)
    selling_price = models.FloatField(null=False)
    purchase_date = models.DateField(auto_now=True)


    def __str__(self):
        return str(self.quantity+self.selling_price)
class Order(models.Model):
    bill_number = models.AutoField(primary_key=True)
    bill_date = models.DateField(auto_now=True)
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    bill_total = models.FloatField()

    def __str__(self):
        return str(self.bill_number+self.customer_name)
class OrderLines(models.Model):
    bill_number = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=120)
    quantity = models.FloatField()
    amount = models.FloatField()

    def __str__(self):
        return str(self.bill_number)


