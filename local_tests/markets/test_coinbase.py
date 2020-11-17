import os
# noinspection PyPackageRequirements
import pytest

from bit_help.markets import Coinbase


def secret_variable(name):
    return os.environ.get("secrets.{}".format(name))


api_key = secret_variable("coinbase_api_key")
secret_key = secret_variable("coinbase_secret_key")


def test_is_valid_invalid_data():
    response = Coinbase.is_valid(Coinbase.random_api_key, Coinbase.random_api_secret)
    assert response is False


def test_is_valid_valid_data():
    response = Coinbase.is_valid(api_key, secret_key)
    assert response


class TestCoinbase:
    transaction = {
        "amount": {
            "amount": "0.00018936",
            "currency": "BTC"
        },
        "from": {
            "currency": "BTC",
            "resource": "bitcoin_network"
        },
        "id": "3ec9c02d-1df6-5078-aea3-fa004862cab1",
        "native_amount": {
            "amount": "241.14",
            "currency": "RUB"
        },
        "network": {
            "hash": "8864e1dfb0ff5208e1fe0c37cf703dab3e95276cae263e930df111deb420e468",
            "status": "confirmed",
        },
        "resource": "transaction",
        "status": "completed",
        "type": "send",
        "updated_at": "2020-11-16T17:50:53Z"
    }

    def setup(self):
        self.transaction = TestCoinbase.transaction
        self.coinbase = Coinbase(api_key, secret_key)

    # noinspection PyRedundantParentheses
    @pytest.mark.parametrize(("currency"), [
        ("rub"),
        ("usd"),
    ])
    def test_price(self, currency):
        bitcoin_price = self.coinbase.price(currency=currency)
        assert isinstance(bitcoin_price, float) == False

    # noinspection PyRedundantParentheses
    @pytest.mark.parametrize(("confirmations"), [
        (0),
        (1),
        (2),
        (3),
    ])
    def test_address_balance(self, confirmations):
        address_balance = self.coinbase.address_balance(secret_variable("ADDRESS_ID"), confirmations=confirmations)
        assert isinstance(address_balance, float)
