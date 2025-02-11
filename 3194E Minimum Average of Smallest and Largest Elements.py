'''You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages.

Example 1:

Input: nums = [7,8,3,4,15,13,4,1]

Output: 5.5

Explanation:

step	        nums	              averages
0	    [7,8,3,4,15,13,4,1] 	        []
1	       [7,8,3,4,13,4]	            [8]
2	         [7,8,4,4]	               [8,8]
3	           [7,4]	              [8,8,6]
4	             []	                 [8,8,6,5.5]
'''

class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        n = len(nums)
        avg = []
        nums.sort()
        j = n-1
        for i in range(0, n//2):
            avg.append((nums[i] + nums[j]) / 2)
            j -= 1
        return min(avg)

mySol = Solution()
nums = [7,8,3,4,15,13,4,1]
print(mySol.minimumAverage(nums))