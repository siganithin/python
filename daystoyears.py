def daystoyear(days):
    years=days//365
    months=days//30
    print(f"no of years:{years} \n no of months {months}")
days=int(input("Enter no of days:"))
daystoyear(days)