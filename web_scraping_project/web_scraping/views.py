import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from .price_scraping import scraping

def home(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        requested_price = request.POST.get('price')
        mail = request.POST.get('email')
        
        try:
            product_name = scraping(link)
            return HttpResponse(f"Received link: {link} \n The product name: {product_name} \n The requested price: {requested_price} \n The email: {mail}")
        
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Error: {str(e)}")

    # Add a default response for GET requests
    return render(request, 'home.html')