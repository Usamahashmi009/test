# models.py
from django.db import models
from django.utils import timezone
class ItemSize(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Vender(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    quantity = models.IntegerField(default=0,)
    category = models.CharField(max_length=50, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    item_size = models.ForeignKey(ItemSize, on_delete=models.SET_NULL, null=True)
    vender = models.ForeignKey(Vender, on_delete=models.SET_NULL, null=True)


    subtotal = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default=0, blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True)

    
def __str__(self):
    if self.item_size:
        return f'{self.item_size.name} - {self.quantity}'
    else:
        return f'Item {self.pk} - {self.quantity}'
