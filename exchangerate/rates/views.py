from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from rates.models import Currency, ExchangeRate

class IndexView(generic.ListView):
    template_name = 'rates/index.html'
    context_object_name = 'latest_rates_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return ExchangeRate.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = ExchangeRate
    template_name = 'rates/detail.html'