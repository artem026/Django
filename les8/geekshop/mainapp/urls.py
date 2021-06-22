from django.urls import path
from .views import products

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('product/<int:pk>/page/<int:page>/', products, name='page'),
]
