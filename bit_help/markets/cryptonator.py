import cryptonator


class Cryptonator(cryptonator.Cryptonator):
    def __init__(self):
        pass

    @staticmethod
    def price(currency="usd"):
        return cryptonator.get_exchange_rate("btc", currency)
