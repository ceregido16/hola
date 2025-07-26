import sys
try:
    word = input("Enter any word you want: ")
    vocals = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for i in word:
        if i in vocals:
            count += 1
    print(f"The amount of vocals in the word {word} is: {count}")
except ValueError:
    print("Invalid input, please try again, only strings are accepted...")
    sys.exit(1)
