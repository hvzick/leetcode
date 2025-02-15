"""OR 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join([char.lower() for char in s if char.isalnum()])
        return result == result[::-1]
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join([char.lower() for char in s if char.isalnum()])    # converts to list and removes punctuation
        print(result)
        j = len(result)-1
        x = True
        for i in range(0, len(result)//2):
            if result[i] == result[j]:
                print(f"{result[i]}=={result[j]}")
                x = True
            else:
                x = False
                break
            j -= 1
        return x 


mySol = Solution()
s = "A man, a plan, a canal: Panama"
print(mySol.isPalindrome(s))

