import blockcypher


from .. import exceptions


class Blockcypher:
    def __init__(self):
        pass

    @staticmethod 
    def link_to_transaction(txid):
        url = "https://live.blockcypher.com/btc/tx/{}/".format(txid)
        return url
        