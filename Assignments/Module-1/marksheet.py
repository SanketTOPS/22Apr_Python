s1 = int(input("Enter Subject1 Mark:"))
s2 = int(input("Enter Subject1 Mark:"))
s3 = int(input("Enter Subject1 Mark:"))
s4 = int(input("Enter Subject1 Mark:"))

total = s1 + s2 + s3 + s4
print("Toal:", total)

pr = total / 4
print("PR:", pr)

if pr >= 70:
    print("Result:A+")
elif pr >= 60:
    print("Result:A")
elif pr >= 50:
    print("Result:B")
elif pr >= 40:
    print("Result:C")
else:
    print("Result:FAIL")
