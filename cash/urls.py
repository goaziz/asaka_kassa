from django.urls import path

from .views import *


urlpatterns = [
    path('', exchange_list, name="main"),
    path('exchange/', ExchangeCreateView.as_view()),
    path('buy/', posterview, name='buy'),
    path('detail/<int:pk>/', ExchangeDetail.as_view(), name='exchange-detail')
]
