# sum the first 10 numbers
sum = 0
for num in range(1, 101): # last one is excluded, so it goes from 1 to 100
    sum = sum + num # program runs until it is fully executed and value of sum changes each round
print(sum)

# print multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} X {j} = {i*j}") # formatted string is used following curly brackets that substitute its value in the input
    print() # used to separate with a line between code run

# rewrite it using while loop
sum = 0
num = 0
while num <= 100:
    num = num +1
    sum += num  # same thing as sum = sum + num

