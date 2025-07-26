x = int(input("Enter a number: "))
multiple_three = []

for i in range(1, x + 1):
    if i % 3 == 0:
        multiple_three.append(i)

print(f"The multiples of three from 1 to {x} are: {multiple_three}")

b = sum(multiple_three)
print(f"The sum of the multiples of three from 1 to {x} is: {b}")


