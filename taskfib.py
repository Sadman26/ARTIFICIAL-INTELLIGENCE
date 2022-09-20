def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
limit=int(input('Enter Limit: '))
for i in range(limit):
    print(fibonacci(i),end=' ')
#pseduo code for this program
# 1. define a function to calculate fibonacci
# 2. take input from user
# 3. use for loop to print fibonacci series
# 4. print the result
# 5. exit
