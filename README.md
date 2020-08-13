# bit-help

[![Build Status](https://travis-ci.com/daveusa31/bit-help.svg?branch=master)](https://travis-ci.com/daveusa31/bit-help)
[![PyPi Package Version](https://img.shields.io/pypi/v/bit_help.svg?style=flat-square)](https://pypi.python.org/pypi/bit_help)
[![PyPi status](https://img.shields.io/pypi/status/bit_help.svg?style=flat-square)](https://pypi.python.org/pypi/bit_help)
[![Downloads](https://pepy.tech/badge/bit_help)](https://pepy.tech/project/bit_help)
[![Supported python versions](https://img.shields.io/pypi/pyversions/bit_help.svg?style=flat-square)](https://pypi.python.org/pypi/bit_help)


# Установка и использование

```sh
pip3 install bit-help
```

```python
import bit_help
```

# Генерация нового адреса и ключей

```python
import bit_help

network = bit_help.Network()
network.create_address()

print(network.address)
print(network.key.public)
print(network.key.private)
```

# Создание транзакции

```python
import bit_help

network = bit_help.Network()
network.create_address()

transaction = network.send_money("3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69", 0.01, speed="average")
print("Ссылка на транзацию {}".format(transaction.link.blockcypher))
```


# TO DO
- [ ] Добавить в utilits валидатор биткоин адресов формата P2WPKH 
- [X] Добавить гайд, как сгененировать адрес
- [X] Добавить гайд, как отправить монеты
