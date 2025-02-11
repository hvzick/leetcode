'''You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!'''

class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        r = []
        for i in range(0, n):
            s = 0
            if k > 0:                               # when k is positive
                for j in range(1, k+1):             # start j from 1 to k+1
                    s += code[(i+j) % n]            # add next k elements
            elif k == 0:                            # when k is equal to 0
                s = 0
            else:                                   # when k is negative
                for j in range(1, -k+1):            # start j from 1 to -k+1, because k is negative - makes it positive
                    s += code[(i-j) % n]            # add previous k elements
            r.append(s)                             # append s to the list
        return r                                    # return the new list

mySol = Solution()
code1 = [5,7,1,4]
k = 3
code2 = [10,5,7,7,3,2,10,3,6,9,1,6]
k = -4
print(mySol.decrypt(code1, k))
print(mySol.decrypt(code2, k))