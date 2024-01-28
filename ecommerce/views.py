from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to CN334 6410742164 Kandanai Ketkao views!')

def item_view(request, item_id): 
    context_data = {
    "item_id": item_id
}
    return render(request, 'index.html', context = context_data)


def homepage_view(request):
    '''This function renders the homepage'''
    return render(request, 'homepage.html')


def category_view(request, category_id):
    return render(request, 'category.html', {'category_id': category_id})


def product_view(request, product_id):
    
    product = {}  

    context = {
        'product': product
    }
    return render(request, 'product.html', context)


def checkout_view(request):
    
    order_info = {}  
    context = {
        'order_info': order_info
    }
    return render(request, 'checkout.html', context)

def contact_view(request):
    return render(request, 'contact.html')