from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}  
context_dict1 = {'boldmessage1': 'This tutorial has been put together by <Xuyang zheng>'}    
def index(request):
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
    return render(request, 'rango/about.html')
    #return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")
 