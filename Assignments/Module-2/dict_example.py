stdata = {"id": 101, "name": "Sanket", "city": "rajkot"}
# print(stdata)
# print(stdata["name"])
# print("Name:", stdata["name"])
# print(stdata.get("city"))
# print(len(stdata))
# print(stdata.keys())
# print(stdata.values())

"""if "name" in stdata:
    print("Yes..")
else:
    print("Noo")"""


"""if "Sanket" in stdata.values():
    print("Yes..")
else:
    print("Noo")"""

# ----------------------------------- #
print(stdata)

"""for i in stdata:
    print(i)"""


"""for i in stdata.values():
    print(i)"""


"""for i in stdata.items():
    print(i)"""


"""for i, j in stdata.items():
    print(i, j)"""

stdata["id"] = 102
stdata["sub"] = "Python"
# stdata.clear()
# stdata.pop("name")
# del stdata["id"]
# del stdata
# print(stdata)

# newdict = stdata.copy()
# print(newdict)
