def q3(fruits, add, n):
    if add in fruits:
        fruits[add] += n
    else:
        fruits[add] = n
    return fruits

print(q3({'apple': 1}, 'apple', 3))
print(q3({'apple': 1}, 'banana', 1))
print(q3({}, 'apple', 3))