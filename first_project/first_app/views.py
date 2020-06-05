from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me': "Now I am coming from first app"}
    return render(request, 'first_app/index.html',context=my_dict)

def apptwo(response):
    return HttpResponse("<em>My Second App <em>")
