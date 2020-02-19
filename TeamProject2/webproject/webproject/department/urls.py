from django.urls import path
from . import views


app_name = 'department'

urlpatterns = [
 path('index/', views.index, name='index'),
 path('map/', views.map, name='map'),
 path('map_data/', views.map_data, name='map_data'),
 path('addaddress/', views.addaddress, name='addaddress'),
 path('firstpage/', views.firstpage, name='firstpage'),
 path('search/', views.search, name='search'),
 path('detail/', views.detail, name='detail'),
]