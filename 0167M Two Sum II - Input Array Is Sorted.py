'''Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.'''

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        r = []
        n = len(numbers)
        left = 0
        right = n-1
        while left < right:
            if numbers[left] + numbers[right] == target:   
                r.append(left + 1)
                r.append(right + 1)
                return r
            elif numbers[left] + numbers[right] > target:   #sum > target, decrement right pointer because right element is too big to come close to the target
                right -= 1
            else:                                           #sum < target, increment left pointer because left element is too small to come close to the target
                left +=1

mySol = Solution()
numbers = [2,7,11,15]
target = 9
print(mySol.twoSum(numbers, target))