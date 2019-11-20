# coding: utf-8

# Algorithm: FizzBuzz

for (i,j) in enumerate(range(1,31)):
    if j % 3 == 0 and j % 5 == 0:
        print(str(i+1) + " FizzBuzz")

    elif j % 3 == 0:
        print(str(i+1) + " Fizz")

    elif j % 5 == 0:
        print(str(i+1) + " Buzz")

    else:
        print(j)

        
