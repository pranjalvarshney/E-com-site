from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop),
    path('about/',views.about),
    path('contact/',views.contact),
    path('tracker/',views.tracker),
    path('search/',views.search),
    path('product/<int:pid>',views.productview),
    path('checkout/',views.checkout),
    
]