from .. import bitcoinUtilities
from bit_help.network.types.key import key


class Address:
    def __init__(self, address, public_key, private_key):
        self.__address = address
        self.__key = key(public_key, private_key)
        if self.key.private:
            self.__wif = bitcoinUtilities.BitcoinUtilities().privkey_to_wif(private_key)
        else:
            self.__wif = None

    @property
    def address(self):
        return self.__address

    @property
    def key(self):
        return self.__key
    
    @property
    def wif(self):
        return self.__wif
        
    
    def __str__(self):
        response = {
            "key": {
                "public": self.key.public,
                "private": self.key.private,
            },
            "address": self.address,
        }
        return str(response)
    
