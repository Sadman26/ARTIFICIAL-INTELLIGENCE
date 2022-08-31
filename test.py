while True:
    x=int(input("Enter X: "))
    y=int(input('Enter Y: '))
    z=int(input('Enter Z: '))
    if x>y and x>z:
        print(x,'is greatest')
    elif y>x and y>z:
        print(y,'is greatest')
    else:
        print(z,'is greatest')