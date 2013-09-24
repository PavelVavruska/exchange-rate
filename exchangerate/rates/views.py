from django.views import generic
from .models import ExchangeRate


class IndexView(generic.ListView):
    template_name = 'rates/index.html'
    context_object_name = 'latest_rates_list'

    def get_queryset(self):
        query = ExchangeRate.objects.order_by('-date')
        if 'year' in self.kwargs:
            query = query.filter(date__year=self.kwargs['year'])
            if 'month' in self.kwargs:
                query = query.filter(date__month=self.kwargs['month'])
                if 'day' in self.kwargs:
                    query = query.filter(date__day=self.kwargs['day'])
        """Return the last five published polls."""
        return query


class DetailView(generic.DetailView):
    model = ExchangeRate
    template_name = 'rates/detail.html'
    context_object_name = 'exchangerate'
