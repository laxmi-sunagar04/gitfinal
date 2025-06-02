from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.compare_prices, name='compare_prices'),
]
