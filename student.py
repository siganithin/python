studno=int(input("Enter student number:"))
studname=str(input("Enter student name:"))
sub1m=int(input("Enter maths marks:"))
sub2m=int(input("Enter physics marks:"))
sub3m=int(input("enter chemistry marks:"))
totalm=sub1m+sub2m+sub3m
avgm=totalm/3
print("student details:\n student number :",studno,"\n student name :",studname,"\nmarks in maths ","pyhsics","chemistry:",sub1m,sub2m,sub3m,"\navgmarks : ",avgm)