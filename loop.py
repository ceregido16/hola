word = input("Enter any word you want: ")
letter = input("Enter a letter to locate into the word you have chosen right before: ")
count = 0


for i in word:
    if i == letter:
        count += 1

print(f"The amount of {letter}'s in the word {word} is: {count}")