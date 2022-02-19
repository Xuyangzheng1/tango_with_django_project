from django.shortcuts import render
from django.http import HttpRequest
# Import the Category model
from rango.models import Category
from rango.models import Page

def index(request):
    
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]


    context_dict = {}
    
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    # context_dict1['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!,oo'

    return render(request, 'rango/index.html', context=context_dict)
#about index!!!!
def about(request: HttpRequest):
    return render(request, 'rango/about.html')

def show_category(request: HttpRequest, category_name_slug):

    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
# If we can't, the .get() method raises a DoesNotExist exception.
# The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Can we find a category name slug with the given name?
# If we can't, the .get() method raises a DoesNotExist exception.
# The .get() method returns one model instance or raises an exception.


        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
# the database to the context dictionary.
# We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
# Don't do anything -
# the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
     # Go render the response and return it to the client.  
    
    return render(request, 'rango/category.html', context_dict)