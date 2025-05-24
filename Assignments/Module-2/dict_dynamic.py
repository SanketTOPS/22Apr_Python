stdata = {}

keys = ["id", "name", "city"]

for i in keys:
    v = input(f"Enter value of {i}:")
    stdata[i] = v

print(stdata)
