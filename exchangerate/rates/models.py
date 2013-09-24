from django.db import models
from django.template.defaultfilters import slugify


class Currency(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    code = models.CharField(max_length=64)

    def __unicode__(self):
        return self.code


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency)
    date = models.DateField()
    rate = models.FloatField()
    multiplied_by = models.IntegerField()
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.currency.code + str(self.date))

        super(ExchangeRate, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.currency) + ":" + str(self.rate) + "/" +\
               str(self.multiplied_by) + "@" + self.date.strftime('%d.%m.%Y')