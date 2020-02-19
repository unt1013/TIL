from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template import loader
from department.models import departmentStore, store, brand
from django.utils import timezone
import json
from django.core import serializers
from django.db.models import Count

# Create your views here.

def index(request):
    return render(request, 'department/index.html', {})

def map(request):
    return render(request, 'department/map.html')

def map_data(request):
    latest_address_list = store.objects.all()
    lal_json = serializers.serialize('json', latest_address_list)
    return HttpResponse(lal_json, content_type = 'application/json')

def addaddress(request):
    address = Address()
    address.address_text = request.POST['address']
    address.address_comm = request.POST['comment']  
    address.save()
    return HttpResponseRedirect(reverse('department:map'))

def firstpage(request):
    return render(request, 'department/firstpage.html')

def search(request):
    search_text = request.POST['searchText']
    store_dict = {}
    BrandList= brand.objects.filter(brand_name__contains = search_text)
    for row in BrandList :
        if (row.ds.ds_name in store_dict) == False :
            store_dict[row.ds.ds_name] = []
        data = {}     
        data['brand_name']=row.brand_name
        data['store_name']=row.store.store_name
        data['ds']=row.ds.ds_name
        data['store_id']=row.store.id
        addTemp = row.store.address
        data['store_address']= addTemp
        store_dict[row.ds.ds_name].append(data)
    return render(request, 'department/search.html',
        {"result": store_dict, "searchText":search_text})


def detail(request):
    getaddress=request.POST.get('storeaddress')
    
    print("#############",getaddress)
    selectstore= store.objects.get(address=getaddress)
    storeId= selectstore.id
    brandList= brand.objects.filter(store_id=selectstore.id).exclude(brand_theme__contains='편의').exclude(brand_theme__contains='휴게').exclude(brand_theme__contains='서비스')
    
    # floorList= brnad.objects.filter(store_id=selectstore.id).get('')
    floorList= brand.objects.filter(store_id=selectstore.id).values('floor').annotate()
    fl=[]
    for f in floorList:
        fl += list(f.values())
    # 층 정렬
    fl=sorted(list(set(fl)))
    f_b = []
    f_h = []
    f_l = []
    for i in fl :
        if i.startswith('별') or i.startswith('B') :
            f_b.append(i)
        elif len(i) == 3 :
            f_h.append(i)
        else :
            f_l.append(i)

    fl = f_b + f_l + f_h

    

    # return render(request, 'department/detail.html', {"store":selectstore, "brandList":brandList, "floorList":floorList})
    return render(request, 'department/detail.html', {"store":selectstore, "brandList":brandList, "fl":fl})

