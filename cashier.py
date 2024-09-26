class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = 0.00
        print("Please insert coins.")
        coins = ["large dollars", "half dollars", "quarters", "nickels"]
        for x in range(len(coins)):
            coin_amount = float(input("How many " + coins[x] + "?: "))

            if x == 0:  # dollar
                total += 1 * coin_amount
            elif x == 1:  # half dollar
                total += 0.5 * coin_amount
            elif x == 2:  # quarter
                total += 0.25 * coin_amount
            elif x == 3:  # nickel
                total += 0.05 * coin_amount

        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if cost > coins:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif cost <= coins:
            print("Here is $" + str(coins - cost) + " in change.")
            return True
