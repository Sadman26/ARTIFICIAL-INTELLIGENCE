def pattern(x,y):
    for i in range(x,y):
        for j in range(i,i+(y-1)):
            print(j,end="")
        print()
pattern(1,6)

