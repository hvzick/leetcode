def addToArrayForm(num, k):
    n = int("".join(map(str, num)))
    x = n + k
    x = [int(digit) for digit in str(x)]
    return x

num = [1,2,0,0]
k = 34
print(addToArrayForm(num, k))