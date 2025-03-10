divisor = 3
for num in range(0, 12, 3):
    print(num/divisor)

for letter in 'Ahola':
    print(letter)

num = 0
while num <= 5:
    print(num)
    num += 2
print("Out")
print(num)

num = 0
count = 0
while num <= 19:
    if num % 3 == 0:
        count += 1
    num + 1
print("Numbers divisible by 3", count)

for i in range(1, 11):
    for j in range(i, 11):  # Start from i to avoid duplicates
        print(f"{i} * {j} = {i * j}")
