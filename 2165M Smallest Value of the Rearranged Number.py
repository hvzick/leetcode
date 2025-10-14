'''
#TODO You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros. Return the rearranged number with minimal value. Note that the sign of the number does not change after rearranging the digits.
'''

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:                           # Handle zero edge case
            return 0
        if num > 0:                            # Handle positive numbers
            n = sorted(list(str(num)))         # Sort digits in ascending order
            if n[0] == '0':                    # If first digit is 0, find first non-zero
                for i in range(len(n)):
                    if n[i] != '0':            # Found first non-zero digit
                        temp = n[0]            # Swap to avoid leading zero
                        n[0] = n[i]
                        n[i] = temp
                        break
            num = int("".join(n))              # Convert sorted digits back to integer
            return num
        else:                                  # Handle negative numbers
            num = list(str(num))               # Convert to list (includes '-' sign)
            n = sorted(num[1:], reverse=True)  # Sort digits in descending order (skip '-')
            num = int("".join(n))              # Convert back to positive integer
            return -num                        # Return as negative

mySol = Solution()
num = 95005
print(mySol.smallestNumber(num))