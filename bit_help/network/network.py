import bitcoin


from bit_help.network import types



class Network:
    def __init__(self):
        pass
    
    def create_address(self):
        private_key = bitcoin.random_key()
        public_key = bitcoin.privtopub(private_key)
        address = bitcoin.pubtoaddr(public_key)
        
        response = types.Address(address, public_key, private_key)
        
        return response

        