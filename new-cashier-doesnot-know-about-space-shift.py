#   "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
# "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

# 1. Burger
# 2. Fries
# 3. Chicken
# 4. Pizza
# 5. Sandwich
# 6. Onionrings
# 7. Milkshake
# 8. Coke


def get_order(order):

    final_dict = {}
    menu_dict = {
        1: "Burger",
        2: "Fries",
        3: "Chicken",
        4: "Pizza",
        5: "Sandwich",
        6: "Onionrings",
        7: "Milkshake",
        8: "Coke",
    }
    menu_list = []
    for k, v in menu_dict.items():
        menu_list.append(v)

    for i in menu_list:
        i = i.lower()
        specific_count = order.count(i)
        if specific_count > 0:
            final_dict[i] = specific_count

    find_keys = []
    for k, v in final_dict.items():
        tempFinal = []
        for i in range(v):
            tempFinal.append(k)
        find_keys.append(" ".join(tempFinal))

    return " ".join(find_keys).title()


if __name__ == "__main__":
    print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))
