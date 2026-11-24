menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for day in range(number_of_days):
    row = []
    for menu in menus:
        qty = int(input(f"Day {day + 1}, {menu}: "))
        row.append(qty)
    sales.append(row)

print("Total per day: ")
for day in range(number_of_days):
    total_day = 0
    for qty in sales[day]:
        total_day +=  qty
    print(f"Day {day + 1 }: {total_day}")

menu_totals = []
for col in range(len(menus)):
    total_menu = 0
    for row in range(number_of_days):
        total_menu += sales[row][col]
    menu_totals.append((menus[col], total_menu))

print(f"Total per menu: {menu_totals}")

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print(f"Best seller: {best_name} ({best_total})")