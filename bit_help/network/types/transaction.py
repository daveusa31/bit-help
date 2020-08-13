from bit_help import services


class Transaction:
    def __init__(self, txid):
        self.__txid = txid
        self.__link = TransactionLink(txid)
    
    @property 
    def txid(self):
        return self.__txid
    
    @property 
    def link(self):
        return self.__link 

    def __str__(self):
        response = {
            "txid": self.txid,
            "link": {
                "blockcypher": self.link.blockcypher
            }
        }
        return str(response)




class TransactionLink:
    def __init__(self, txid):
        self.__blockcypher = services.Blockcypher.link_to_transaction(txid)
    
    @property
    def blockcypher(self):
        return self.__blockcypher
       
       
    def __str__(self):
        response = {
            "blockcypher": self.__blockcypher,
        }
        return str(response)