from exchangeratesapi import rates
import requests


BASE_URL = 'http://api.exchangeratesapi.io/v1/'
API_KEY = 'e08ed1da10dc39fd4ceea95ec390e712'


def get_currency(base, symbols):
    response = requests.get(BASE_URL+'latest?access_key='+API_KEY+'&base='+base+'&symbols='+symbols)
    data = response.json()
    return data


base = 'EUR'
symbols = 'RUB'
get_currency(base, symbols)