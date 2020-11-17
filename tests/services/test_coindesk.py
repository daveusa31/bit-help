import os
import sys
import random
# noinspection PyPackageRequirements
import pytest

import bit_help


class TestCoindesk:
    def setup(self):
        self.coindesk = bit_help.services.Coindesk()

    def test_price(self):
        assert isinstance(self.coindesk.price(), float)

    def test_historical_data(self):
        assert isinstance(self.coindesk.historical_data(), dict)

    def test_supported_currencies(self):
        assert isinstance(self.coindesk.supported_currencies(), list)

    @pytest.mark.parametrize(("currency"), [
        ("test"),
    ])
    def test_price_invalid_currency(self, currency):
        try:
            response = self.coindesk.price(currency=currency)
        except bit_help.exceptions.InvalidCurrency:
            response = bit_help.exceptions.InvalidCurrency

        assert bit_help.exceptions.InvalidCurrency == response
