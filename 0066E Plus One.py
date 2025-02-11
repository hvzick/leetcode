def plusOne(digits):
    x = ""
    for i in range(0, len(digits)):
        x = x + str(digits[i])
    print(x)
    x = int(x) + 1
    x = str(x)
    t = list(map(int, x))
    return t

digit = [4,3,2,1]
print(plusOne(digit))