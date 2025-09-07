def calculate_total(cart):
    total_amount = 0
    prices = list(cart.values())
    for price in prices:
        total_amount += price
    if len(prices) > 5:
        total_amount -= (total_amount * 10) / 100
        return int(total_amount)
    else:
        return total_amount


shopping_cart = {'Laptop': 50000,'Headphones': 50000,'Mouse': 50000,'Keyboard': 50000,'Mic': 50000,'Speaker': 50000}
print(calculate_total(shopping_cart))
