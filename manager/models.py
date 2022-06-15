from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=30, default="")
    lot_number = models.CharField(null=True, blank=True,max_length=50)
    exp_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.item_name
