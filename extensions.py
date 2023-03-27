import requests
import json


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        r = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}&symbols={sym}")
        resp = json.loads(r.content)
        new_price = resp['rates'][sym] * float(amount)
        return new_price