import validators

from . import markets


def format_sum(_sum):
    return "{:.8f}".format(_sum)


def convert_satoshis_to_bitcoins(sum_in_satoshis: int, number_of_digits: int = 8):
    """
    Конвертации суммы в сатошах в биткоины
    Параметры:
    ----------
    sum_satoshis : int
        Сумма в сатошах
    number_of_digits : Optional[int]
        Количество чисел после запятой

    Returns
    -------
    float

    """
    _len = 8 - len(str(sum_in_satoshis))  # Сколько нулей нужно ещё до 8
    _sum = "0.{}{}".format("0" * _len, sum_in_satoshis)  # И создаётся сумма с нулями
    _sum = round(float(_sum), number_of_digits)
    return _sum


def convert_bitcoins_to_satoshis(sum_in_bitcoins: float):
    """
    Конвертации суммы в биткоинах в сатоши
    Параметры:
    ----------
    sum_in_bitcoins : float
        Сумма в биткоинах

    Returns
    -------
    int

    """
    sum_in_satoshis = int(sum_in_bitcoins * 100000000)
    return sum_in_satoshis


def address_validate(address: str):
    if validators.btc_address(address):
        response = True
    else:
        response = False

    return response


def convert_fiat_to_bitcoin(_sum: float, currency: str, bitcoin_price: int = None):
    """
    Конвертация фиатной суммы в биткоины
    Parameters
    ----------
    _sum : str
        Сумма, ко
    currency : str
        Валюта на входе. Например: rub, btc
    bitcoin_price: int
        Цена биткоина

    Returns
    -------
    float
    """
    if bitcoin_price is None:
        bitcoin_price = markets.Cryptonator().price(currency=currency)

    sum_in_bitcoin = round(_sum / int(bitcoin_price), 8)
    return sum_in_bitcoin


def convert_bitcoin_to_fiat(_sum_in_bitcoin: float, need_currency: str, bitcoin_price: int = None):
    if bitcoin_price is None:
        bitcoin_price = markets.Cryptonator().price(currency=need_currency)

    sum_in_fiat = round(_sum_in_bitcoin * bitcoin_price, 2)
    return sum_in_fiat
