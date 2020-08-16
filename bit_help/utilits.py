import validators




def format_sum(sum):
    return "{:.8f}".format(sum) 


def convert_satoshis_to_bitcoins(sum_in_satoshis: int, number_of_digits: int=8):
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
    _len = 8 - len(str(sum_in_satoshis)) # Сколько нулей нужно ещё до 8
    sum = "0.{}{}".format("0"*_len, sum_in_satoshis) # И создаётся сумма с нулями
    sum = round(float(sum), number_of_digits)
    return sum


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



# def convert(sum: float, now_currency: str, need_currency: str, btc_price: str=None):
#     """
#     Конвертация валюты в другую
#     Parameters
#     ----------
#     sum : str
#         Сумма на входе
#     now_currency : str
#         Валюта на входе. Например: rub, btc, sts
#     need_currency: str
#         Нужна валюта на выходе
#     sum : float
#         Сумма перевода. Обязательно в рублях
#     comment : Optional[str]
#         Комментарий к платежу
    
#     Returns
#     -------
#     float
#     """
#     print(helper.get_btc_price())
#     # fiat_currencyes = ["rub", "usd"]
#     # crypto_currencyes = ["btc", "sts"]

#     # assert False == now_currency in fiat_currencyes + crypto_currencyes
#     # assert False == need_currency in fiat_currencyes + crypto_currencyes



#     # if now_currency in fiat_currencyes or need_currency in fiat_currencyes:
#     #     if now_currency in fiat_currencyes:
#     #         currency = now_currency

#     #     elif need_currency in fiat_currencyes:
#     #         currency = need_currency

#     #     btc_price = self.price(currency=currency)


#     # if "btc" == now_currency and "sts" == need_currency:
#     #     response = utilits.convert_bitcoins_to_satoshis(sum)

#     # elif "sts" == now_currency and "btc" == need_currency:
#     #     response = utilits.convert_satoshis_to_bitcoin(sum)

#     # elif now_currency in crypto_currencyes and need_currency in fiat_currencyes:
#     #     if "sts" == now_currency:
#     #         sum_in_btc = utilits.convert_satoshis_to_bitcoin(sum)

#     #     elif "btc" == now_currency:
#     #         sum_in_btc = sum

#     #     response = btc_price * sum_in_btc


#     # return response
