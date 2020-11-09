import pytest

from bit_help.markets import Coinbase


def test_coinbase_is_valid_invalid_data():
    response = Coinbase.is_valid(Coinbase.random_api_key, Coinbase.random_api_secret)
    assert response is False
