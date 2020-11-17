import random
# noinspection PyPackageRequirements
import pytest

import bit_help


class TestBlockcypher:
    url_to_transaction = "https://live.blockcypher.com/btc/tx"
    url_to_transaction += "/559e8a3544438ff4b93f02e53d41589659f7ec54855a1d0d40eb6fc71c811515/"

    def setup(self):
        self.blockcypher = bit_help.services.Blockcypher()

    def test_link_to_transaction(self):
        txid = "559e8a3544438ff4b93f02e53d41589659f7ec54855a1d0d40eb6fc71c811515"
        assert self.blockcypher.link_to_transaction(txid) == TestBlockcypher.url_to_transaction
