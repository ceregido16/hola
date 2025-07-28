sentence = input("Enter a sentence: ")
sentence = sentence.lower()
sentence = sentence.split() #divide the string guided by all the blank spaces
dict = {}

for word in sentence:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for word in dict:
    print(f"The word {word} appears {dict[word]} times.")