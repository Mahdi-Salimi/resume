from django.urls import path

from .views import home_view, service_detail_view, portfolio_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('service_detail', service_detail_view, name='service-detail'),
    path('portfolio_detail', portfolio_detail_view, name='porfolio-detail')
]