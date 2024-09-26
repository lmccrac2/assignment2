from data import resources, recipes
from cashier import Cashier
from sandwich_maker import SandwichMaker

# Make an instance of other classes here
resources = resources
recipes = recipes
sandwich_machine = SandwichMaker(resources)
cashier = Cashier()


class Main:
    not_off = True  # variable representing turning off the machine

    while not_off:
        command = input("What would you like? small/ medium/ large/ off/ report): ")

        # used match because it's better than a lot of ifs
        match command:
            case "off":  # ends loop and program
                not_off = False
            case "report":  # reports resources
                print("Bread: " + str(resources["bread"]) + " slice(s)")
                print("Ham: " + str(resources["ham"]) + " slices(s)")
                print("Cheese: " + str(resources["cheese"]) + " pound(s)")
            case "small" | "medium" | "large":
                order_recipe = recipes[command]
                if sandwich_machine.check_resources(order_recipe["ingredients"]):
                    if cashier.transaction_result(cashier.process_coins(), order_recipe["cost"]):
                        sandwich_machine.make_sandwich(command, order_recipe["ingredients"])
            case _:
                print("Invalid input. Try again")

