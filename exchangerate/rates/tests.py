# coding=UTF-8

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class LoadingTest(TestCase):
    def test_parsing(self):
        from .utils import get_currencies
        raw_data = """
27.09.2013 #189
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|17,668
Brazílie|real|1|BRL|8,397
Bulharsko|lev|1|BGN|13,135
Čína|renminbi|1|CNY|3,102
Dánsko|koruna|1|DKK|3,445
EMU|euro|1|EUR|25,690
"""
        output_data = [{'name': 'dolar', 'country': 'Austrálie', 'code': 'AUD'},
                       {'name': 'real', 'country': 'Brazílie', 'code': 'BRL'},
                       {'name': 'lev', 'country': 'Bulharsko', 'code': 'BGN'},
                       {'name': 'renminbi', 'country': 'Čína', 'code': 'CNY'},
                       {'name': 'koruna', 'country': 'Dánsko', 'code': 'DKK'},
                       {'name': 'euro', 'country': 'EMU', 'code': 'EUR'}]
        data = get_currencies(raw_data)

        self.assertEqual(output_data, data)