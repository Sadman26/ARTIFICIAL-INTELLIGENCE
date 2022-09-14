def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
limit=int(input('Enter Limit: '))
for i in range(limit):
    print(fib(i),end=' ')