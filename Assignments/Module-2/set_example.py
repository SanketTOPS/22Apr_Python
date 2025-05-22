myset = {"a", "b", "c", "d", "e", "a", "b"}
# print(myset)
# print(len(myset))

"""for i in myset:
    print(i)
"""

# --------------------- #
# print(myset)
# myset.add("f")
# myset.remove("d")
# myset.pop()
# myset.clear()
# x = myset.copy()
# print(x)


# ---------------------------- #
print(myset)

newset = {"x", "y", "z", "a", "c"}
print(newset)
# x = myset.union(newset)
x = myset.intersection(newset)
print(x)
