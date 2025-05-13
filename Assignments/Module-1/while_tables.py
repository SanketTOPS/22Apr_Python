n = int(input("How many tables you want? : "))

i = 1

while i <= n:
    tb = int(input("Enter any number for your Table:"))  # 3
    j = 1
    while j <= 10:
        print(f"{tb}*{j}={tb * j}")
        j += 1
    i += 1
