LAST_DIGIT = 5  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
total = 0
limit = 0
for i in range(7):
    expense = int(input("Enter : "))
    expenses.append(expense)

highest = expenses[0]

for index, i in enumerate(expenses):
    if i > daily_limit:
        limit += 1
    if i > highest :
        highest = i
        highest_output = f"Highest: day {index + 1} ({i})"
    total += i
    print(f"Day {index + 1}: {i}")

print(f"Daily Limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {total/len(expenses):.1f}")
print(f"Highest: {highest_output}")
print(f"Days above limit: {limit}")
