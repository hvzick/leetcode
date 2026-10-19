'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''

class Solution:
    def threeSum(self, nums: list) -> list[list]:  
        n = sorted(nums)
        res = []
        for i in range(len(n)):
            if i > 0 and n[i] == n[i-1]: continue
            if n[i] > 0: break
            j = i + 1
            k = len(n) - 1
            while j < k:
                current_sum = n[i] + n[j] + n[k]
                if current_sum == 0:
                    res.append([n[i], n[j], n[k]])
                    j += 1
                    k -= 1
                    while j < k and n[j] == n[j-1]:
                        j += 1
                    while j < k and n[k] == n[k+1]:
                        k -= 1
                elif current_sum < 0:
                    j += 1
                else:
                    k -= 1
        return res

mySol = Solution()
nums = [-1,0,1,2,-1,-4]
print(mySol.threeSum(nums))