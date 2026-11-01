str1 = input("Enter first word: ").lower()
str2 = input("Enter second word: ").lower()

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")
