from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from django.views.generic import DetailView

from .serializers import ExchangeSerializer
from .models import Exchange, CurrencyRate, Case
from .forms import *



def index(request):
    return render(request, 'apps/index.html', {})

def exchange_list(request):
    rates = Exchange.objects.all()
    return render(request, 'apps/index.html', {'rates': rates})

class ExchangeCreateView(ListCreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer


#    def perform_create(self, serializer):
#        serializer.save(user=self.request.user)

def sell_currency(request):
    return render(request, 'exchange_detail.html', {})

def posterview(request):
    template_name = 'test.html'
    myform = Myform(request.POST or None)
    rates = CurrencyRate.objects.all()
    cases = Case.objects.all()
    context = {
        'myform': myform,
        'rates': rates,
        'cases': cases
    }
    return render(request, template_name, context)


class ExchangeDetail(DetailView):
    model = Exchange
    template_name = 'exchange_detail.html'