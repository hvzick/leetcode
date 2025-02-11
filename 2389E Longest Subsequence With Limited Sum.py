'''You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
'''
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        m = len(queries)
        answer = []
        for i in range(0, m):
            count = 0
            sum = 0
            for j in range(0, n):
                if nums[j] + sum <= queries[i]:
                    sum += nums[j]
                    count += 1
            answer.append(count)
        return answer

mySol = Solution()
nums = [469781,45635,628818,324948,343772,713803,452081]
queries = [816646,929491]
print(mySol.answerQueries(nums, queries))