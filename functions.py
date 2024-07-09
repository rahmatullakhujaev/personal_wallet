from datetime import date
from action import Action
def display_balance():
    '''Displays current balance'''
    with open('balance.txt', 'r') as file:
        balance = int(file.read())
    print(balance, ' $')

def get_balance():
    """Get current balance as variable"""
    with open('balance.txt', 'r') as file:
        balance = int(file.read())
    return balance
def date_converter(date_str):
    """Converts input date into datetime date type """
    date_list = date_str.split('-')
    try:
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])
        converted_date = date(year, month, day)
        return converted_date
    except:
        return "Date input invalid!"


def add_income(date, amount, description):
    """Records new income to file and updates balance"""
    with open('income.txt', 'a') as file:
        file.write(f"{date}/{amount}/{description}\n")
    current_balance = get_balance()
    with open('balance.txt', 'w') as file:
        file.write(str(current_balance+amount))




def add_consumption(date, amount, description):
    """Records new consumption to file and updates balance"""
    with open('consumption.txt', 'a') as file:
        file.write(f"{date}/{amount}/{description}\n")
    current_balance = get_balance()
    with open('balance.txt', 'w') as file:
        file.write(str(current_balance-amount))

def get_income():
    """Returns all income records as list"""
    with open('income.txt', 'r') as file:
        income =file.readlines()
    income_list = []
    for i in income:
        i1 = i.split('/')
        date = i1[0]
        amount = i1[1]
        description = i1[2]
        i2 = Action('income', date, amount, description)
        income_list.append(i2)
    return income_list

def get_consumption():
    """Returns all consumption records as list"""
    with open('consumption.txt', 'r') as file:
        consumption =file.readlines()
    consumption_list = []
    for i in consumption:
        i1 = i.split('/')
        date = i1[0]
        amount = i1[1]
        description = i1[2]
        i2 = Action('consumption', date, amount, description)
        consumption_list.append(i2)
    return consumption_list



