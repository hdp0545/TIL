def q4(word):
    for w in word:
        if w in 'safy':
            return True
    return False

print(q4('fish'))
print(q4('galaxy'))
print(q4('united'))