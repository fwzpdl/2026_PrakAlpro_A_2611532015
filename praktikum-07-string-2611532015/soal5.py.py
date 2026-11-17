# Name: Muhammad Fawwaz
# NIM: 2611532015
# Question 5

# bagian A 
username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")

elif not username.isalnum():
    print("Invalid: letters and digits only")

elif not username[0].isalpha():
    print("Invalid: must start with a letter")

else:
    print("Valid")

# bagian B 

nim = "2611532015"

if len(nim) == 10 and nim.isdigit():
    print(f"Valid, intake year 20{nim[:2]}")

else:
    print("Invalid NIM")