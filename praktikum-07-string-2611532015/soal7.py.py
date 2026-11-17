# Name: Muhammad Fawwaz
# NIM: 2611532015
# Question 7

full_name = "muhammad fawwaz"
nim = "2611532015"

clean_name = full_name.lower().strip()
position_space = clean_name.find(" ")

if position_space == -1:
    first_name = clean_name

else:
    first_name = clean_name[:position_space]

print("="*30)
print(f"{"STUDENT CARD":^30}")
print("="*30)
print(f"Name\t\t: {full_name.title()}")
print(f"NIM\t\t: {nim}")
print(f"Username\t: {first_name + nim[-3:]}") # kalau pakai satu tab semua jadinya tidak rapi pak
print(f"Intake\t\t: 20{nim[:2]}")
print("="*30)