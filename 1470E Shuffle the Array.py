'''Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].'''

class Solution:
    def shuffle(self, nums:list[int], n: int) ->list[int]:
        shuffled = []
        j = n                               # start from n till 2n
        for i in range(0, n):
            shuffled.append(nums[i])        # append elements till n           
            shuffled.append(nums[j])        # append elements till 2n     
            j += 1                          # increment j
        return shuffled                     # return the shuffled list


mySol = Solution()
nums = [2,5,1,3,4,7]
n = 3
print(mySol.shuffle(nums, n))