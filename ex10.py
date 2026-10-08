def give_ticket_by_category(category_name:str, price:float, amount:int):
    if amount != 0:
        average = price/amount
    else:
        average = 0
    s = f"{amount} products are in the category {category_name}\nTotal cost: {price}\nAverage price per product {average}"
    return s

beverages_total = 0
beverages_amount = 0

fruit_total = 0
fruit_amount = 0

vegetable_total = 0
vegetable_amount = 0

amount = int(input("Specify the number of products you wish to enter: "))

for i in range(amount):
    category = str(input("What is the category? [V: Vegetables, F: Fruit, B: Beverages]"))
    price = float(input("What is the cost price of the product?"))
    if category == "V":
        vegetable_total = vegetable_total+price
        vegetable_amount += 1
    elif category == "B":
        beverages_total = beverages_total+price
    else:
        fruit_amount +=1
        fruit_total = fruit_total+price

print(give_ticket_by_category("Vegetabables", vegetable_total, vegetable_amount))
print(give_ticket_by_category("fruit", fruit_total, fruit_amount))
print(give_ticket_by_category("beverages", beverages_amount, beverages_total))
