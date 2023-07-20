from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    context = {
        'title':'Home Page'
    }
    return render(request, 'main.html', context)
