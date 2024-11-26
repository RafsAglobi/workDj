from django.urls import path
from task4.views import shop, cart, home

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
]
