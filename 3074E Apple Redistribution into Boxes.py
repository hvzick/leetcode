'''You are given an array apple of size n and an array capacity of size m.

There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.

Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.

Note that, apples from the same pack can be distributed into different boxes.'''

class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        count = sum(apple)                  # count number of apples
        capacity.sort(reverse=True)         # sort the capacities in reverse
        counter = 0
        for i in range(0, len(capacity)):   # loop over capacities
            if count > 0:                   # check if there are any apples left
                count -= capacity[i]        # subtract the capacity from apples
                counter += 1                # increment the counter
            else:                           # when there are no apples left
                break                       # break
        return counter
            
        
mySol = Solution()
apple = [9,8,8,2,3,1,6]
capacity = [10,1,4,10,8,5]
print(mySol.minimumBoxes(apple, capacity))