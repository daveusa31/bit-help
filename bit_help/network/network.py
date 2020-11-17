import bit
import random
import bitcoin
import requests
import bitcoinfees 
import blockcypher


from .. import utilits
from bit_help import exceptions
from bit_help.network import types


class Network(types.Address):
    __AVAILABLE_FEES = {
        "min": "fastestFee", 
        "average": "halfHourFee", 
        "max": "hourFee",
    }
    
    def __init__(self, address=None, public_key=None, private_key=None):
        super().__init__(address, public_key, private_key)
        self.bit_key = bit.PrivateKey(super().wif)
        
    def create_address(self):
        private_key = bitcoin.random_key()
        public_key = bitcoin.privtopub(private_key)
        address = bitcoin.pubtoaddr(public_key)

        response = types.Address(address, public_key, private_key)
        super().__init__(address, public_key, private_key)

        return response

    def transaction_history(self):
        return bitcoin.history(self.address)

    def send_money(self, address, _sum, fee_or_speed="average"):
        """
        Speed min, average, max
        """
        fee = self.__commission_calculate(fee_or_speed)
        output = [(address, _sum, "btc")]
        
        txid = self.bit_key.send(output, fee=fee)
        response = types.Transaction(txid)
        return response

    def balance(self, service="random"):
        if "random" == service:
            service = random.choice(["blockcypher", "bit"])
        
        if "blockcypher" == service:
            balance_in_satoshis = blockcypher.get_total_balance(self.address)
        elif "bit" == service:
            balance_in_satoshis = self.bit_key.get_balance()
            
        balance_in_bitcoins = utilits.convert_satoshis_to_bitcoins(balance_in_satoshis)
        return balance_in_bitcoins

    def __commission_calculate(self, fee_or_speed):
        if isinstance(fee_or_speed, float):
            fee = fee_or_speed
        elif fee_or_speed in self.__AVAILABLE_FEES:
            fee = bitcoinfees.recommended()[self.__AVAILABLE_FEES[fee_or_speed]]
        else:
            available_speeds = [speed for speed in self.__AVAILABLE_FEES]
            raise exceptions.InvalidSpeed("Invalid speed name. Available speeds: {}".format(available_speeds))

        return fee
