def strong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum =sum+factorial(digit)
        temp = temp // 10
    return n == sum
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter a number: "))
if strong_number(num):
    print("{} [Strong Number]".format(num))
else:
    print("{} [Weak Number]".format(num))
#pseduo code for this program
# 1. define a function to calculate factorial
# 2. define a function to calculate strong number
# 3. take input from user
# 4. use if else statement to print strong number
# 5. print the result
# 6. exit