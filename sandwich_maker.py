from data import resources
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        low_item = ""
        if resources["bread"] >= ingredients["bread"]:
            if resources["ham"] >= ingredients["ham"]:
                if resources["cheese"] >= ingredients["cheese"]:
                    return True
                else:
                    low_item = "cheese"
            else:
                low_item = "ham"
        else:
            low_item = "bread"

        print("Sorry not enough" + low_item)
        return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources
           Hint: no output"""
        # deduct ingredients
        resources.update({"bread": resources["bread"] - order_ingredients["bread"]})
        resources.update({"ham": resources["ham"] - order_ingredients["ham"]})
        resources.update({"cheese": resources["cheese"] - order_ingredients["cheese"]})
        print(sandwich_size + " sandwich is ready. Bon appetit!")