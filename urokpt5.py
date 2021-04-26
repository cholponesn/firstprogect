data = {
    'glock.20':2000,
    'usp':2500,
    'fs':3467,
    'deagle':5000,
    'p92':4000,
    'colt':90000,
    'magnum':6000,
    'p90':10000,
    'mp7':11000,
    'uzi':12000,
    'mp5':14000,
    'm16':20000,
    'ak-47':19000,
    'm416':24000,
    'famas':21000,
    'AWM':30000,
    'Dragunov':31000,
    'Barett':50000,
    'RPG':100000,
    'Topol-M':2000000}


"""
ТЗ:
По данным введенным пользователем вычислить, сможет он купить выбранный им товар или нет.
Если товар в списке отсутствует - NOT OK
__________
Входные данные: название товара,кол-во товара, наличные
Реализовать 2+ функциями
Выходные данные: словарь состящий из: 
{названия товара как ключ:кол-во, следующий элемент - потраченная сумма - ключ, значение сумма}
"""


weapon = input()
quantity = int(input())
money = int(input())
def count_payback(price,quantity,money):
    payback = quantity * price
    if money >= payback:
        return money - payback
    else:
        return 'Недостаточно средств'
def shop(weapon_name,quantity,money):
    if weapon_name in data:
        price = data[weapon_name]
        payback = count_payback(price,quantity,money)
        if isinstance(payback,int):
            result = {weapon_name:quantity,'total_sum':price*quantity}
        else:
            result = payback
        print(result)
    else:
        print('We have no {}!'.format(weapon_name))
shop(weapon,quantity,money)

