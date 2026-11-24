LAST_DIGIT = 5
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for i in range(7):
    expense = int(input(f"Day {i + 1}: "))
    expenses.append(expense)

total = 0
days_above_limit = 0

highest = expenses[0]
highest_day = 1

for index, expense in enumerate(expenses):
    total += expense

    if expense > daily_limit:
        days_above_limit += 1

    if expense > highest:
        highest = expense
        highest_day = index + 1

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {total / len(expenses):.1f}")
print(f"Highest: day {highest_day} ({highest})")
print(f"Days above limit: {days_above_limit}")