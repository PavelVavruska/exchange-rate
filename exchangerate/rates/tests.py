# coding=UTF-8

from django.test import TestCase
from datetime import date

from django.test.client import Client


class SimpleTest(TestCase):
    def setUp(self):
        # Set up Client
        self.client = Client()

    def test_rates_index(self):
        # GET request of Rates index page
        response = self.client.get('/rates/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class LoadingTest(TestCase):
    def test_get_url(self):
        from .utils import get_url
        cnb_prefix_url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
        cnb_test_url = "".join([cnb_prefix_url, "?date=11.9.2013"])
        test_date = date(2013, 9, 11)
        self.assertEqual(get_url(test_date), cnb_test_url)

    def test_parsing_exchange_rates(self):
        from .utils import get_exchange_rates
        raw_data = """27.09.2013 #189
        země|měna|množství|kód|kurz
        Austrálie|dolar|1|AUD|17,668
        Brazílie|real|1|BRL|8,397
        Bulharsko|lev|1|BGN|13,135
        Čína|renminbi|1|CNY|3,102
        Dánsko|koruna|1|DKK|3,445
        EMU|euro|1|EUR|25,690
        Filipíny|peso|100|PHP|43,744"""
        output_data = [{'code': 'AUD', 'date': '27.09.2013', 'rate': '17,668', 'multiplied_by': '1'},
                       {'code': 'BRL', 'date': '27.09.2013', 'rate': '8,397', 'multiplied_by': '1'},
                       {'code': 'BGN', 'date': '27.09.2013', 'rate': '13,135', 'multiplied_by': '1'},
                       {'code': 'CNY', 'date': '27.09.2013', 'rate': '3,102', 'multiplied_by': '1'},
                       {'code': 'DKK', 'date': '27.09.2013', 'rate': '3,445', 'multiplied_by': '1'},
                       {'code': 'EUR', 'date': '27.09.2013', 'rate': '25,690', 'multiplied_by': '1'},
                       {'code': 'PHP', 'date': '27.09.2013', 'rate': '43,744', 'multiplied_by': '100'}]
        data = get_exchange_rates(raw_data)
        self.assertEqual(output_data, data)

    def test_parsing_currencies(self):
        from .utils import get_currencies
        raw_data = """27.09.2013 #189
        země|měna|množství|kód|kurz
        Austrálie|dolar|1|AUD|17,668
        Brazílie|real|1|BRL|8,397
        Bulharsko|lev|1|BGN|13,135
        Čína|renminbi|1|CNY|3,102
        Dánsko|koruna|1|DKK|3,445
        EMU|euro|1|EUR|25,690
        Filipíny|peso|100|PHP|43,744"""
        output_data = [{'name': 'dolar', 'country': 'Austrálie', 'code': 'AUD'},
                       {'name': 'real', 'country': 'Brazílie', 'code': 'BRL'},
                       {'name': 'lev', 'country': 'Bulharsko', 'code': 'BGN'},
                       {'name': 'renminbi', 'country': 'Čína', 'code': 'CNY'},
                       {'name': 'koruna', 'country': 'Dánsko', 'code': 'DKK'},
                       {'name': 'euro', 'country': 'EMU', 'code': 'EUR'},
                       {'name': 'peso', 'country': 'Filipíny', 'code': 'PHP'}]
        data = get_currencies(raw_data)
        self.assertEqual(output_data, data)