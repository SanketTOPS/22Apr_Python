def sum(a, b):
    print("Sum:", a + b)


def sub(a, b):
    print("Sub:", a - b)


def mul(a, b):
    print("Mul:", a * b)


no1 = int(input("Enter Number1:"))
no2 = int(input("Enter Number2:"))
print("1:Sum")
print("2:Sub")
print("3:Mul")
choice = int(input("Select your choice:"))


if choice == 1:
    sum(no1, no2)
elif choice == 2:
    sub(no1, no2)
elif choice == 3:
    mul(no1, no2)
else:
    print("Error!Invalid choice...")
