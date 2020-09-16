from django.urls import path

from .views import *

urlpatterns = [
    path('', exchange_list, name="main"),
    path('exchange/', ExchangeCreateView.as_view()),
    path('buy/', posterview, name='buy'),
    path('sell/', sell_currency, name='sell'),
	]