"""
Menus:
1. Show balance
2. Income menu
3. Consumptions menu

2.1. Search for income
2.2. Show all income
2.3  Add new income
2.4  Back

3.1. Search for income
3.2. Show all income
3.3  Add new income
3,4  Back

Needed functions:

1.get_balance()
2.display_balance()
3.get_income()
"""

from datetime import date
from action import Action
from functions import *

print("Welcome!")

option = 1

while option != 0:
    print('Select an option:\n\n1.Balance\n2.Income menu\n3.Consumption menu\n0.Exit')
    option = int(input())

    if option == 1:
        display_balance()
    elif option == 2:
        sec_op = 1
        while sec_op != 0:
            print("Select menu:\n1. Search for income\n2. Show all income\n3. Add new income\n0. Back")
            sec_op = int(input())

            if sec_op == 1:
                date = input("Input date(YYYY-MM-DD): ")
                income_list = get_income()
                sorted_list = []
                for income in income_list:
                    if income.get_date() == date:
                        sorted_list.append(income)
                print("#\tDate\tAmount\tDescription\n")
                for i in range(len(sorted_list)):
                    income = sorted_list[i]
                    print(f"{i + 1}.\t{income.get_date()}\t{income.get_amount()}\t{income.get_description()}")
            elif sec_op == 2:
                income_list = get_income()
                print("#\tDate\tAmount\tDescription\n")
                for i in range(len(income_list)):
                    income = income_list[i]
                    print(f"{i+1}.\t{income.get_date()}\t{income.get_amount()}\t{income.get_description()}")
            elif sec_op == 3:
                check = True
                while check:
                    date = input("Date(YYYY-MM-DD): ")
                    date = date_converter(date)
                    if type(date) == type('a'):
                        print(date)
                    else:
                        check = False
                amount = int(input("Amount: "))
                description = input("Description: ")
                add_income(date,amount,description)
                print("Income added!")

    elif option == 3:
        sec_op = 1
        while sec_op != 0:
            print("Select menu:\n1. Search for consumption\n2. Show all consumptions\n3. Add new consumption\n0. Back")
            sec_op = int(input())

            if sec_op == 1:
                date = input("Input date(YYYY-MM-DD): ")
                consumption_list = get_consumption()
                sorted_list = []
                for consumption in consumption_list:
                    if consumption.get_date() == date:
                        sorted_list.append(consumption)
                print("#\tDate\tAmount\tDescription\n")
                for i in range(len(sorted_list)):
                    consumption = sorted_list[i]
                    print(f"{i + 1}.\t{consumption.get_date()}\t{consumption.get_amount()}\t{consumption.get_description()}")
            elif sec_op == 2:
                consumption_list = get_consumption()
                print("#\tDate\tAmount\tDescription\n")
                for i in range(len(consumption_list)):
                    consumption = consumption_list[i]
                    print(f"{i + 1}.\t{consumption.get_date()}\t{consumption.get_amount()}\t{consumption.get_description()}")
            elif sec_op == 3:
                check = True
                while check:
                    date = input("Date(YYYY-MM-DD): ")
                    date = date_converter(date)
                    if type(date) == type('a'):
                        print(date)
                    else:
                        check = False
                amount = int(input("Amount: "))
                description = input("Description: ")
                add_consumption(date, amount, description)
                print("Consumption added!")



