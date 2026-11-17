# Name: Muhammad Fawwaz
# NIM: 2611532015
# Question 3

# A 
text = "Informatika"
print(text[-1])
print(text.upper())
print(text)

# B 
text = "Muhammad Fawwaz"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)


