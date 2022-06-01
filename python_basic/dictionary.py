dict = {"name": "pey", "phone": "1110000"}


print(dict)
print(type(dict))
print(dir(dict))
# print(dict(dict))


dict2 = {"1": [1, 2, 3]}


dict2["2"] = [4, 5, 6]


print(dict2["2"])


# del dict2["2"]
print(dict2)


print(dict2.keys())

print(list(dict2.keys()))


print(dict2.values())

print(dict2.items())
