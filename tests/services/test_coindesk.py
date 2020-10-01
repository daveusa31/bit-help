import os
import sys
import random
import pytest


import bit_help


coindesk = bit_help.services.Coindesk()



def test_price():
    assert isinstance(coindesk.price(), float)

def test_historical_data():
    assert isinstance(coindesk.historical_data(), dict)

def test_supported_currencies():
    assert isinstance(coindesk.supported_currencies(), list)