from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def service_detail_view(request):
    return render(request, 'service-details.html')

def portfolio_detail_view(request):
    return render(request, 'portfolio-details.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')