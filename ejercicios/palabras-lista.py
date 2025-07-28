sentence = input("Enter a sentence: ")
sentence = sentence.lower()
sentence = sentence.split()
dict = {}

for word in sentence:
    if word not in dict:
        list_word = []
        for letter in word:
            if letter not in list_word:
                dict[word] = list_word
                list_word.append(letter)
    else:
        continue


print(dict)


