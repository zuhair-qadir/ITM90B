from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    clientID = models.CharField(max_length=200)
    companyname = models.CharField(max_length=200, null=True)
    companyemail = models.CharField(max_length=200)
    companyaddress = models.CharField(max_length=200)

    def __str__(self):
        return self.companyname

class Tool(models.Model):
    toolID = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class RentalOrder(models.Model):
    orderID = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)
    tool_specification = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(RentalOrder, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(RentalOrder, on_delete=models.SET_NULL, null=True)
	shippingaddress = models.CharField(max_length=200, null=False)
	shippingcity = models.CharField(max_length=200, null=False)
	shippingprovince = models.CharField(max_length=200, null=False)
	shippingpostalcode = models.CharField(max_length=200, null=False)

	def __str__(self):
		return self.shippingaddress