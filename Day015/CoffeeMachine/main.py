from coffee_functions import decide_action

resource_stats = ""



# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "


user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

decide_action(user_selection)
