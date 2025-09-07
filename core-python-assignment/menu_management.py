def adding_item(menu, item):
    if item not in menu:
        menu.append(item)
    return menu
def removing_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(item, "is not available")
    return menu
def checking_item(menu, item):
    if item in menu:
        print(f'Availability: "{item} is available"')
    else:
        print(f'Availability: "{item} is not available"')


initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
menu = adding_item(initial_menu, add_item)
remove_item = "Salad"
menu = removing_item(menu, remove_item)
print("Updated menu:", menu)
check_item = "Pizza"
checking_item(menu, check_item)
