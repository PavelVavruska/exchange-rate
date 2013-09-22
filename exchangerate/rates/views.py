from django.views import generic
from django.shortcuts import get_object_or_404

from rates.models import Currency, ExchangeRate

class IndexView(generic.ListView):
    template_name = 'rates/index.html'
    context_object_name = 'latest_rates_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return ExchangeRate.objects.order_by('-date')[:5]


class DetailView(generic.DetailView):
    model = ExchangeRate
    template_name = 'rates/detail.html'
    context_object_name = 'exchangerate'
