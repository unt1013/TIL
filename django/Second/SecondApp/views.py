from django.shortcuts import render
from django.http import HttpResponse
from SecondApp.models import Curriculum
# Create your views here.


def index1(request):
    return HttpResponse('<h1>Hello</h1>')
def index2(request):
    return HttpResponse('<h2>Hello</h2>')
def index3(request):
    return HttpResponse('<h3>Hello</h3>')

def main(request):
    datalist = Curriculum.objects.all()
    html = ''
    for cur in datalist:
        html += cur.name + '<br>'
    return render(request,'secondapp/show.html', {'list':datalist})