from django.contrib import admin
from rates.models import Currency, ExchangeRate

class ExchangeRateInline(admin.TabularInline):
    model = ExchangeRate
    extra = 3

class CurrencyExchangeRate(admin.ModelAdmin):
    inlines = [ExchangeRateInline]

admin.site.register(Currency, CurrencyExchangeRate)