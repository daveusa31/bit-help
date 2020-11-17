import requests
import datetime


from .. import exceptions


class Coindesk:
    """
    Доступные методы:
        price
        historical_data
        supported_currencies
    """
    __API_URL = "https://api.coindesk.com/v1/bpi/"
    

    def __init__(self):
        self.__supported_currencies = self.supported_currencies()

    def price(self, currency="USD"):
        currency = currency.upper()
        self.__check_currency(currency=currency)

        path = "currentprice/{}.json".format(currency)
        price = float(self.__request(path)[currency]["rate_float"])
        return price

    def historical_data(self, start="2013-09-01", end=None):
        if not end:
            end = datetime.datetime.now().strftime('%Y-%m-%d')

        path = "historical/close.json"
        params = {
            "start": start,
            "end": end,
        }
        return self.__request(path, params=params)

    def supported_currencies(self):
        _supported_currencies = []
        path = "supported-currencies.json"
        supported_currencies_and_countries = self.__request(path, use_bpi=False)

        for currency_and_country in supported_currencies_and_countries:
            currency = currency_and_country["currency"]
            _supported_currencies.append(currency)

        return _supported_currencies



    def __check_currency(self, currency):
        if not currency in self.__supported_currencies:
            raise exceptions.InvalidCurrency(currency)

    def __request(self, path, params=(), use_bpi=True):
        url = self.__API_URL + path
        response = requests.get(url, params=params).json()

        response = response["bpi"] if use_bpi else response
        return response