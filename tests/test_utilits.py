import os
import sys
import random
import pytest


import bit_help


    

@pytest.mark.parametrize(("sum_in_satoshis", "need_sum_in_bitcoins"), [
    (50000, 0.0005),
    (55000, 0.00055),
])
def test_convert_satoshis_to_bitcoins(sum_in_satoshis, need_sum_in_bitcoins):
    sum_in_bitcoins = bit_help.utilits.convert_satoshis_to_bitcoins(sum_in_satoshis)

    # print("Ковертация {} сатошей в биткоины".format(sum_in_satoshis))
    # text = "Должно выйти {}. На выходе {}"
    # print(text.format(need_sum_in_bitcoins, sum_in_bitcoins))
    
    assert sum_in_bitcoins == need_sum_in_bitcoins



@pytest.mark.parametrize(("address"), [
    ("3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69"),
])
def test_address_validate(address):
    assert bit_help.utilits.address_validate(address)
    


@pytest.mark.parametrize(("sum_in_bitcoins", "need_sum_satoshis"), [
    (0.0005, 50000),
    (0.00055, 55000),
])
def test_convert_bitcoins_to_satoshis(sum_in_bitcoins, need_sum_satoshis):
    sum_in_satoshis = bit_help.utilits.convert_bitcoins_to_satoshis(sum_in_bitcoins)
    
    assert sum_in_satoshis == need_sum_satoshis

