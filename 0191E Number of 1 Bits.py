def hammingWeight(n: int) -> int:
    b = bin(n)
    count = 0
    for i in range(2, len(b)):
        if b[i] == '1':
            count += 1
    return int(count)

n = 11
print(hammingWeight(n))
