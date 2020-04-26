from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop),
    path('about/',views.about),
    path('contact/',views.contact),
    path('tracker/',views.tracker),
    path('search/',views.search),
    path('productview/',views.productview),
    path('checkout',views.checkout),
    
]