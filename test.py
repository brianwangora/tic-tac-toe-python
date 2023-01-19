def whileloop(i):
    while i < 10:
        print (i)
        i += 1
    else:
        print("i is no longer less than 10")
print (whileloop(0))


fruits = ["mango", "pineapple", "apple", "strawberry"]
def forloop():
    for x in fruits:
        if x == "apple":
            break
        print(x)

print (forloop())

# Using the range() function

for x in range(9):
    print(x*9)
else:
    print("We're through!!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# Nested Loop
for x in adj:
  for y in fruits:
    print(x, y)

# The Pass Statement
for x in [0,1,2]:
    pass


# // Returns the integer value of the quotient

print(906/10)
print(906//10)

# % Returns the remainder in division
print(7%2)
print(7/2)

num = 2

lower = -20
upper = 50

print("These are prime numbers between", lower, "and", upper,".")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# In an if function, elif is short for "else if"