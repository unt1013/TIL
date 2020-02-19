from django.db import models
from django.db.models import Count

# Create your models here.
class departmentStore(models.Model):
    ds_name=models.CharField(max_length=255)

class store(models.Model):
    store_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    store_time=models.CharField(max_length=255)
    phone_num=models.CharField(max_length=255)
    ds=models.ForeignKey(departmentStore, on_delete=models.CASCADE)
    img = models.CharField(max_length = 512, default = 'charField')
    def __str__(self):
        return str(self.ds)

class brand(models.Model):
    brand_name=models.CharField(max_length=255)
    brand_theme=models.CharField(max_length=255)
    floor=models.CharField(max_length=50)
    store=models.ForeignKey(store, on_delete=models.CASCADE)
    ds=models.ForeignKey(departmentStore, on_delete=models.CASCADE)


