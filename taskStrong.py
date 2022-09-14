
def strong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += factorial(digit)
        temp //= 10
    return n == sum

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
if strong(num):
    print(num,"is a strong number")
else:
    print(num,"is not a strong number")