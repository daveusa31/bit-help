from bit_help.network.types.key import key


class Address:
    def __init__(self, address, public_key, private_key):
        self.__address = address
        self.__key = key(public_key, private_key)
    
    @property
    def address(self):
        return self.__address

    @property
    def key(self):
        return self.__key
    
    def __str__(self):
        response =  "Private key: {}\nPublic key: {}\nAddress: {}\n"
        response = response.format(self.key.public, self.key.public, self.address)
        return reponse
    
