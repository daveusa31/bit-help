import random
# noinspection PyPackageRequirements
import pytest

import bit_help
from bit_help import exceptions


class TestNetwork:
    bitcoin_address = "37RhAm18qGyTBxnkt7uHEaTuBGnYjpVcU6"
    txid = "559e8a3544438ff4b93f02e53d41589659f7ec54855a1d0d40eb6fc71c811515"

    def setup(self):
        self.network = bit_help.network.Network()
        self.network.create_address()

    def test_transaction_history(self):
        assert 0 == len(self.network.transaction_history())

    # noinspection PyRedundantParentheses
    @pytest.mark.parametrize(("speed"), [
        ("min"),
        ("average"),
        ("max"),
        0.0000001
        ])
    def test_send_money_valid_commission(self, speed):
        try:
            response = self.network.send_money(self.bitcoin_address, 0.000001, fee_or_speed=speed)
        except ValueError:
            response = ValueError

        assert ValueError == response

    def test_send_money_invalid_commission(self):
        try:
            response = self.network.send_money(self.bitcoin_address, 0.000001, fee_or_speed="wsdefrtgy")
        except exceptions.InvalidSpeed:
            response = KeyError

        assert KeyError == response

    # noinspection PyRedundantParentheses
    @pytest.mark.parametrize(("service"), [
            ("blockcypher"),
            ("bit"),
    ])
    def test_balance(self, service):
        balance = self.network.balance(service=service)
        assert isinstance(balance, float)

    def test_balance_random(self):
        assert isinstance(self.network.balance(), float)

    def test_str_address(self):
        public_key = self.network.key.public
        response = str(bit_help.network.types.Address(self.network.address, public_key, self.network.key.private))
        assert isinstance(response, str)

    def test_transaction(self):
        transaction = bit_help.network.types.Transaction(self.txid)
        assert isinstance(str(transaction), str)

    def test_str_transaction_link(self):
        transaction = bit_help.network.types.Transaction(self.txid)
        assert isinstance(str(transaction.link), str)
