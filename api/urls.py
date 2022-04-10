from django.urls import path
from api.views import *

urlpatterns = [
    path('products/', Product.as_view(), name='products')
]
