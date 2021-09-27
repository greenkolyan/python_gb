price = [57.8, 46.51, 97, 65.4, 73.3, 91.56, 22, 156.2, 529, 25.76]
print(price)
for cost in price:
    rub = int(cost)
    penny = (cost - rub) * 100
    print(f'{rub} руб {penny:02.0f} коп')

price = [57.8, 46.51, 97, 65.4, 73.3, 91.56, 22, 156.2, 529, 25.76]
print(price)
print(id(price))
price.sort()
print(id(price))
for cost in price:
    rub = int(cost)
    penny = (cost - rub) * 100
    print(f'{rub} руб {penny:02.0f} коп')

price = [57.8, 46.51, 97, 65.4, 73.3, 91.56, 22, 156.2, 529, 25.76]
print(price)
for cost in sorted(price)[::-1][:5]:
    rub = int(cost)
    penny = (cost - rub) * 100
    print(f'{rub} руб {penny:02.0f} коп')

print([f'{int(cost)} руб {(cost - int(cost)) * 100:02.0f} коп' for cost in sorted(price)[::-1][:5]])
