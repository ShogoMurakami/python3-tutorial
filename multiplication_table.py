# coding: utf-8

# Multiplication table (九九)

def multiply(x,y):
    return x * y

for step in range(1,10):
    for num in range(1,10):
        print(multiply(step,num), end="")
        if num < 9:
            print(",", end="")

    print("")
