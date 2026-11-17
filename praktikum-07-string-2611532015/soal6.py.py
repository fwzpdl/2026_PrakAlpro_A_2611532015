# Name: Muhammad Fawwaz
# NIM: 2611532015
# Question 6

full_name = "Muhammad Fawwaz"
nim = "2611532015"

clean_name = full_name.lower().strip()
position_space = clean_name.find(" ")

if position_space == -1:
    first_name = clean_name

else:
    first_name = clean_name[:position_space]

print(first_name + nim[-3:])