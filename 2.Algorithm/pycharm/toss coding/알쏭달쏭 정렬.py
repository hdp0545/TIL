data = list(input().split())
key = ["8", "5", "2", "4", "3", "7", "6", "1", "0", "9"]
data.sort(key=lambda x: key.index(x))
print(" ".join(data))