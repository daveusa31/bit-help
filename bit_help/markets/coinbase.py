import random_data
import blockcypher

from coinbase.wallet.client import Client


from .. import utilits
from .. import exceptions


class Coinbase(Client):
    random_api_key = random_data.etc.password(length=5)
    random_api_secret = random_data.etc.password(length=5)

    """
    Доступные методы:
        price
        address_balance
    """


    def __init__(self, api_key: str=random_api_key, api_secret: str=random_api_secret):
        super().__init__(api_key, api_secret) # Наследуем класс coinbase
        self.__client = Client(api_key, api_secret)
        self.__account_id = self.__client.get_primary_account()["id"]

    @property
    def client(self):
        return self.__client

    @property
    def account_id(self):
        return self.__account_id




    def price(self, currency="USD"):
        currency_pair = "BTC-{}".format(currency.upper()) 
        price = self.client.get_sell_price(currency_pair=currency_pair)
        return float(price["amount"])


    def address_balance(self, address_id, confirmations=1):
        balance = 0

        data = self.client.get_address_transactions(self.account_id, address_id)
        transactions = data["data"]


        if 0 < len(transactions):
            for transaction in transactions:
                hash = transaction["network"]["hash"] # Txid
                transaction_sum = float(transaction["amount"]["amount"]) # Сумма транзакции в виде 0.001 btc


                if 3 <= confirmations:
                    """
                    Если нужно 3 или больше подтверждений сети,
                    то проверяется транзакция на coinbase
                    """
                    if self.__check_confirmation_from_coinbase(transaction):
                        balance += transaction_sum
                    

                elif confirmations in [1, 2]:
                    """
                    Если нужно 2 или 3 конфирма
                    """
                    transaction_info = blockcypher.get_transaction_details(hash)

                    if "confirmations" in transaction_info:
                        transaction_confirmations = transaction_info["confirmations"]

                    elif self.__check_confirmation_from_coinbase(transaction):
                        transaction_confirmations = 3

                    else:
                        transaction_confirmations = 0


                    if confirmations <= transaction_confirmations:
                        balance += transaction_sum


                elif 0 == confirmations:
                    balance += transaction_sum



        return balance


    def __check_confirmation_from_coinbase(self, transaction):
        if "confirmed" == transaction["network"]["status"]:
            response = True
        else:
            response = False

        return response
