# Name: Muhammad Fawwaz
# NIM: 2611532015
# Bonus Question

kalimat = input("Masukkan kalimat: ")
teks = kalimat.lower().replace(" ", "")

if teks == teks[::-1]:
    print("Palindrome")

else:
    print("Not a palindrom")
