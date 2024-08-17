from django.shortcuts import render


def home_view(request):
    context = get_about_context()
    return render(request, 'index.html', context)

def service_detail_view(request):
    return render(request, 'service-details.html')

def portfolio_detail_view(request):
    return render(request, 'portfolio-details.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    context = get_about_context()
    return render(request, 'about.html', context)

def portfolios_view(request):
    return render(request, 'portfolios.html')

def services_view(request):
    return render(request, 'services.html')

def get_about_context():
    return {
        'name': 'Mahdi',
        'profile': 'Backend Developer',
        'email': 'example@gmail.com',
        'phone': '01234567890'
    }