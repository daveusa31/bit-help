import random
# noinspection PyPackageRequirements
import pytest

import bit_help
from bit_help import exceptions


class TestNetwork:
    bitcoin_address = "37RhAm18qGyTBxnkt7uHEaTuBGnYjpVcU6"

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
