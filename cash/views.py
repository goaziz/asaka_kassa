from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.generics import ListCreateAPIView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .serializers import ExchangeSerializer
from .models import Exchange, CurrencyRate, Case
from .forms import *


def index(request):
    return render(request, 'apps/index.html', {})


@login_required
def exchange_list(request):
    rates = Exchange.objects.filter(user=request.user).order_by('-id')
    return render(request, 'apps/index.html', {'rates': rates})


class ExchangeCreateView(ListCreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer


#    def perform_create(self, serializer):
#        serializer.save(user=self.request.user)

@login_required
def posterview(request):
    template_name = 'test.html'
    myform = Myform(request.POST or None)
    rates = CurrencyRate.objects.all().order_by('id')
    cases = Case.objects.all()
    context = {
        'myform': myform,
        'rates': rates,
        'cases': cases
    }

    return render(request, template_name, context)


class ExchangeDetail(LoginRequiredMixin, DetailView):
    model = Exchange
    template_name = 'exchange_detail.html'
