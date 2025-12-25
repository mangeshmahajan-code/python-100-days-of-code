MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0 ,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coffe_bill (menu,useer_response,user_paid_coin,user_choice):
    """Return the change or tell for inscient amount"""
    cost=menu[useer_response]["cost"]
    if user_paid_coin > cost :
        return f"Here is ${user_paid_coin-cost} in change.\nHere is your {user_choice} ☕️. Enjoy!"
    else:
        return  "Sorry that's not enough money. Money refunded."


def resource (present_resources_list,coffe_resource_details):
    """Return 0 when the resources are not enough """
    if present_resources_list["water"]<coffe_resource_details["water"]:
        print("Sorry there is not enough water.")
        return 0
    elif present_resources_list["milk"]<coffe_resource_details["milk"]:
        print("Sorry there is not enough milk.")
        return 0
    elif present_resources_list["coffee"]<coffe_resource_details["coffee"]:
        print("Sorry there is not enough coffee.")
        return 0
    else:
        return 1

def report(present_resources_list,coffe_resource_details):
        """Give the recorce report """
        return {
                "water": present_resources_list["water"]-coffe_resource_details["water"],
                "milk": present_resources_list["milk"]-coffe_resource_details["milk"],
                "coffee": present_resources_list["coffee"]-coffe_resource_details["coffee"],
        }



on_off="on"
coin_amount =0
while on_off=="on":
    user_coffe_type=input("What would you like? (espresso/latte/cappuccino/off):").lower()

    if user_coffe_type=="off":
        on_off="off"
        print("Thanks for using coffee machine.")
    elif user_coffe_type=="report":
        print(f"Water : {resources["water"]}ml\nMilk : {resources["milk"]}ml\nCoffee : {resources["coffee"]}g\nMoney : {coin_amount}")

    else:
        coffe_details=MENU[user_coffe_type]["ingredients"]
        # print (coffe_details)
        remaining_resources = resource(resources, coffe_details)
        if remaining_resources ==1:
            numbers_of_pennies = int(input("Please insert coin \nhow many pennies?: "))
            numbers_of_nickles = int(input("how many nickles?: "))
            numbers_of_dimes = int(input("how many dimes?: "))
            numbers_of_quarters = int(input("how many quarters?: "))
            paid_coin_amount =(numbers_of_pennies*0.01)+(numbers_of_nickles*0.05)+(numbers_of_dimes*0.10)+(numbers_of_quarters*0.25)
            # print(paid_coin_amount)
            coin_amount += MENU[user_coffe_type]["cost"]
            display_bill_status=coffe_bill(MENU,user_coffe_type,paid_coin_amount,user_coffe_type)
            print(display_bill_status)
            resources=report(resources,coffe_details)
        else:
            on_off="off"
