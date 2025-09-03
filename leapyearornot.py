def leap(year):
    if(year%4 == 0 or year%400 == 0):
        print(f"{year} is leapyear")
    else:
        print(f"{year} is not a leapyear")
n=int(input("Enter a year:"))
leap(n)