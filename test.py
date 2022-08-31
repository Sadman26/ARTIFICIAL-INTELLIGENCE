while True:
    def compare(x,y,z):
        if x>y and x>z:
            print(x,'is greatest than ',y,' and ',z)
        elif y>x and y>z:
            print(y,'is greatest than ',x,' and ',z)
        else:
            print(z,'is greatest than ',x,' and ',y)
    x=int(input("Enter X: "))
    y=int(input('Enter Y: '))
    z=int(input('Enter Z: '))
    compare(x,y,z)
    