def greater(a,b,c):
    if a>b and a>c:
        if b>c and a>b :
            print("a is greater")
        else:
            print("b is greater")
    else:
        print("c is greater")
a,b,c=map(int,input("enter values ").split(","))
greater(a,b,c)