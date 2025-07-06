import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def currency_conversion(summa, currency):
    """ Функция обращения к внешнему API"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={summa}"
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)

    return response.json()['result']
