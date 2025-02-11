'''You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false'''

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] != 1 and n <= 1:# check if there is only 1 element in the list and that too is zero so that we can plant one flower
            return True
        count = 0
        new = flowerbed                                         # we do not need to copy the list but its runtime is less on leetcode somehow
        for i in range(0, len(flowerbed)):
            #print(f'count = {count}')
            #rint(f'i = {i}')
            if flowerbed[i] == 1:                               # check if current value is 1 
                continue                                        # when its one, skip
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:   # check if you are at first index and its adjacent is zero
                    new[i] = 1                                  # plant here 
                    count += 1                                  # increment the count
            elif i == len(flowerbed)-1:                         # check if we are at last element
                if flowerbed[i-1] == 0:                         # check if the previous element is 0
                    new[i] = 1                                  # plant here
                    count += 1                                  # increment the count
            else:               
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0: # check if adjacent values are 0
                    new[i] = 1                                  # plant here
                    count += 1                                  # increment the count
        if count >= n:                                          # check if the count is >= n
            return True                                         # if yes return true
        else:
            return False                                        # if no return false

mySol = Solution()
flowerbed = [1,0,0,0,0,1]
n = 2
print(mySol.canPlaceFlowers(flowerbed, n))