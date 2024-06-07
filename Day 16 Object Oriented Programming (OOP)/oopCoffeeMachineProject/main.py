from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino/):"
#  a. Check the user's input to decide what to do next.
#  b. The prompt should show every time action has completed, e.g. once the drink is is dispensed. The prompt should
#     show again to serve the next customer. Done
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_coffe_machine_run = True
while is_coffe_machine_run:
    drink_order = input(f"What would you like? ({menu.get_items()}): ").lower()
# TODO 2. Turn off the Coffee Machine by entering "off" to the prompt. DONE
#  a. For maintainers of the coffee machine, they can use "off" as the secret word to turn off the machine. Your code
#     should end execution when this happens. DONE
    if drink_order == "off":
        is_coffee_machine_run = False
        break
# TODO 3. Print report. DONE
#   a. When the user enters "report" to the prompt, a report should be generated that shows the current resource values.
#      e.g.
#      Water: 100ml
#      Milk: 50ml
#      Coffee: 76g
#      Money: $2.5 DONE
    elif drink_order == "report":
        coffee_maker.report()
        money_machine.report()
        continue
# TODO 4. Check resources sufficient?
#   a. When the user chooses a drink, the program should check if there are enough resources to make that drink. DONE
#   b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make
#      the drink but print: "Sorry there is not enough water". DONE
#   c. The same should happen if another resource is depleted, e.g. milk or coffee. DONE
    drink_order = menu.find_drink(drink_order)
    if drink_order is None:
        continue
    if coffee_maker.is_resource_sufficient(drink_order) is False:
        continue
# TODO 5. Process coins. DONE
#   a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert
#      coins. Done
#   b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 DONE
#   c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x
#      2 + 0.05 + 0.01 x 2 = $0.52 DONE
    if coffee_maker.is_resource_sufficient(drink_order) is True:
        money_machine.process_coins()
# TODO 6. Check Transaction successful?
#   a. Check that the user has inserted enough money to purchase the drink they selected. E.g. Latte cost $2.50, but
#      the only inserted $0.52 then after counting the coins the program should say "Sorry that's not enough money.
#      Money refunded." DONE
#   b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit
#      and this will be reflected the next time "report" is triggered. E.g.
#      Water: 100ml
#      Milk: 50ml
#      Coffee: 76g
#      Money: $2.5 DONE
#   c. If the user has inserted too much money, the machine should offer change. E.g. "Here is $2.45 dollars in change."
#      The change should be rounded to 2 decimal places. DONE
    is_transaction_successful = money_machine.make_payment(drink_order.cost)
    if is_transaction_successful is False:
        continue
# TODO 7. Make Coffee. DONE
#   a. If the transaction is successful and there are enough resources to make the drink the user selected, then the
#      ingredients to make the drink should be deducted from the coffe machine resources.
#      E.g. report before purchasing latte:
#      Water: 300ml
#      Milk: 200ml
#      Coffee: 100g
#      Money: $0
#      Report after purchasing latte:
#      Water: 100ml
#      Milk: 50ml
#      Coffee: 76g
#      Money: $2.5 DONE
#   b. Once all resources have been deducted, tell the user "Here is your latte. Enjoy!". If latte was their choice of
#      drink. DONE
    if is_transaction_successful is True:
        coffee_maker.make_coffee(drink_order)
        continue
