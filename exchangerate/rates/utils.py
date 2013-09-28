from textwrap import dedent

def get_url(date):
    """Returns full url with correct data format."""
    url = ""
    return url


def get_raw_data(url):
    """Returns data from url as list of strings."""
    raw_data = ['', '', '']
    return raw_data


def get_currencies(raw_data):
    """Returns a list of currencies in a particular date."""
    line_number = 0
    data_array = []
    content = raw_data.splitlines()
    for line_of_text in content:
        line_number += 1
        # FIND NEEDED HTML ROW
        if line_number > 2:
            line_array = dedent(line_of_text).split('|')
            actual_currency = {'name': line_array[1], 'country': line_array[0], 'code': line_array[3]}
            data_array.append(actual_currency)
    return data_array


def get_exchange_rates(raw_data):
    """Returns exchange rates for currencies in a particular date."""
    data = ['', '', '']
    return data