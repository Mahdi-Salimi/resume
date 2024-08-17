from django.urls import path

from .views import home_view, service_detail_view, portfolio_detail_view, contact_view, about_view, portfolios_view, services_view

urlpatterns = [
    path('', home_view, name='home'),
    path('service_detail', service_detail_view, name='service-detail'),
    path('portfolio_detail', portfolio_detail_view, name='porfolio-detail'),
    path('contact', contact_view, name='contact'),
    path('about', about_view, name='about'),
    path('portfolios', portfolios_view, name='portfolios'),
    path('services', services_view, name='services')

]