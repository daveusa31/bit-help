import bit
import random
import bitcoin
import blockcypher


from .. import utilits
from bit_help.network import types



class Network(types.Address):
    def __init__(self, address=None, public_key=None, private_key=None):
        super().__init__(address, public_key, private_key)
        self.bit_key = bit.PrivateKey(super().wif)
        
    def create_address(self):
        private_key = bitcoin.random_key()
        public_key = bitcoin.privtopub(private_key)
        address = bitcoin.pubtoaddr(public_key)

        response = types.Address(address, public_key, private_key)

        return response

    def transaction_history(self):
        return bitcoin.history(self.address)

    def send_money(self, address, sum):
        # mktx
        pass

    def balance(self):
        service = random.choice(["blockcypher","bit",])
        
        if "blockcypher" == service:
            balance_in_satoshis = blockcypher.get_total_balance(self.address)
        elif "bit" == service:
            balance_in_satoshis = self.bit_key.sget_balance()
            
        balance_in_bitcoins = utilits.convert_satoshis_to_bitcoins(balance_in_satoshis)
        return balance_in_bitcoins


