import bitcoin
import blockcypher


from .. import utilits
from bit_help.network import types



class Network:


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
        balance_in_satoshis = blockcypher.get_total_balance(self.address)
        balance_in_bitcoins = utilits.convert_satoshis_to_bitcoins(balance_in_satoshis)
        return balance_in_bitcoins

