cno=int(input("Enter consumer number"))
cname=input("Enter name:")
pmr=int(input("Enter present month reading:"))
lmr=int(input("Enter last month reading:"))
totalunits=pmr-lmr
bill=totalunits*3.80
print("total bill:",bill)
print(f"consumerno{cno} \n consumer name {cname} \n presentmonthreading {pmr} \nlastmonthreading {lmr} \n total bill {bill} ")