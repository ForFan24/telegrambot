import requests
import json
from config import keys


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        r = requests.get(f"https://v6.exchangerate-api.com/v6/e21dbbcf2b432f56c7a3a4b0/pair/{quote_ticker}/{base_ticker}")
        resp = json.loads(r.content)
        new_price = resp["conversion_rate"]* amount
        new_price = round(new_price, 3)
        message = f"Стоимость {amount} {quote} в {base} : {new_price}"
        return message