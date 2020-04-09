from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me': "I am inside shiv_first_app/index.html"}
    return render(request, 'shiv_first_app/index.html', context= my_dict)
