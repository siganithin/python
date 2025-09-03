def divby5and11(num):
    if(num%5 == 0 and num%11 == 0):
        print(f"{num} is divisible by both")
    else:
        print(f"{num} is not divisible by both")
n=int(input("Give a number:"))
divby5and11(n)
    