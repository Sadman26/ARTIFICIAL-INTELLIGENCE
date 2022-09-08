start = int(input("Enter Starting: "));
end = int(input("Enter a range : "))
while(start <= end):
    n = start
    status = 0
    i = 2
    while(i < n):
        if(n % i == 0):
            status = 1
            break
        i = i + 1
    start = start + 1
    if(status == 0):
        print(start-1,end=' ')
