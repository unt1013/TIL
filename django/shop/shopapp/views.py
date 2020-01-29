from django.shortcuts import render
from django.http import HttpResponse
from .models import shop

# Create your views here.

def Shop(request):
    shopdata = shop.objects.all()
    html =''
    for c in shopdata:
        html += str(c.id) + '\n' + c.shop_name + '\n' + c.shop_desc + '\n' + c.rest_date + '\n' + c.parking_info + '\n' + c.img_path + '\n' + '=============='
    return render(request, 'shopapp/shop.html', {'list':html})