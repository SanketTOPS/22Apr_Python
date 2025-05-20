tech = ["c", "c++", "html", "css", "java"]
"""print(tech)
print(tech[0])
print(tech[-1])
print(tech[0:3])
print(tech[2:])
print(tech[:3])"""

# print(len(tech))

# ---------------------------------- #
# print(tech)
# tech[2] = "Python"
# print(tech)

"""for i in tech:
    print(i)"""

"""n = 0
for i in tech:
    print(f"{n} - {i}")
    n += 1"""

"""if "html" in tech:
    print("Yes...")
else:
    print("Noo")"""


# print(tech.index("c++"))

"""for i in tech:
    print(f"{tech.index(i)} - {i}")"""

# -------------------------------------- #
print(tech)
# tech.append("python")
# tech.insert(2, "php")
# tech.remove("java")
# tech.pop()
# tech.pop(0)
# tech.clear()
# tech.reverse()
# tech.sort()
# del tech
# print(tech)


# newlist = tech.copy()
# print(newlist)

newlist = ["PHP", "NODE", "REACT"]
print(newlist)

# print(tech + newlist)
tech.extend(newlist)
print(tech)
