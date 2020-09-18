from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse


class CurrencyRate(models.Model):
    name = models.CharField(max_length=100)
    buy_rate = models.DecimalField(max_digits=100, null=True, decimal_places=2)
    sell_rate = models.DecimalField(max_digits=100, null=True, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Case(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exchange(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    summa = models.DecimalField(max_digits=200, decimal_places=2)
    rate = models.ForeignKey(CurrencyRate, on_delete=models.DO_NOTHING)
    case = models.ForeignKey(Case, on_delete=models.DO_NOTHING)
    check = models.CharField(max_length=250, blank=True, null=True)
    total_sum = models.DecimalField(null=True, blank=True, max_digits=200, decimal_places=2)
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('exchange-detail', kwargs={'pk': self.pk})


def check_save(instance, sender, **kwargs):
    if kwargs['created']:
        case = instance.case
        rate = instance.rate
        if case.id == 1:
            instance.total_sum = instance.summa * rate.buy_rate
            instance.check = 'A - 0' + str(instance.id)
        elif case.id == 2:
            instance.total_sum = instance.summa * rate.sell_rate
            instance.check = 'B - 0' + str(instance.id)
        instance.save()


post_save.connect(receiver=check_save, sender=Exchange)
