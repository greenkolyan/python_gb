import utils

currency = input('Введите валюту, которую нужно перевести в рубли: ')
print(utils.currency_rates(currency))
