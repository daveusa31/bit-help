import bit
import random
import bitcoin
import requests
import bitcoinfees 
import blockcypher


from .. import utilits
from bit_help.network import types



class Network(types.Address):
    __AVIABLE_FEES = {
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

    def send_money(self, address, sum, fee=None, speed=None):
        """
        Speed min, average, max
        """
        fee = self.__commission_calculate(fee, speed)
        output = [(address, sum, "btc")]
        
        txid = self.bit_key.send(output, fee=fee)
        response = types.Transaction(txid)
        return response

    def balance(self):
        service = random.choice(["blockcypher","bit",])
        
        if "blockcypher" == service:
            balance_in_satoshis = blockcypher.get_total_balance(self.address)
        elif "bit" == service:
            balance_in_satoshis = self.bit_key.get_balance()
            
        balance_in_bitcoins = utilits.convert_satoshis_to_bitcoins(balance_in_satoshis)
        return balance_in_bitcoins

    
    def __commission_calculate(self, fee, speed):
        if fee or speed:
            if 0 < fee:
                response = fee
            elif speed:
                if speed in self.__AVIABLE_FEES: 
                    response = bitcoinfees.recommended()[self.__AVIABLE_FEES[speed]]
                else:
                    exception_text = "Invalid speed. Aviable {}"
                    raise ValueError(exception_text.format(self.__AVIABLE_FEES))
        else:
            response = bitcoinfees.recommended()[self.__AVIABLE_FEES["average"]]
        
        return response
                
        


