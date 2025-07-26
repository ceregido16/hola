word = input("Enter any word you want and then I will tell you if it is a palindrome or not: ")
list = []

for i in word:
    list.append(i)
    

list2 = list[::-1]

if list == list2:
    print(f"The word {word} is a palindrome")
else:
    print(f"The word {word} is not a palindrome")