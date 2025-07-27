word = input("Tell me a word and I will tell you if it has repeated letters: ")
word = word.lower()
repeated_letters = {}

for letter in word:
    if letter in repeated_letters:
        repeated_letters[letter] += 1
    else:
        repeated_letters[letter] = 1
    
for letter in repeated_letters:
    print(f"The letter {letter} appears {repeated_letters[letter]} times in the word {word}. ")