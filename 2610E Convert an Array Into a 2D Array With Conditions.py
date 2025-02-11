'''You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.'''

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        newList = []                            # initialise new list to store the 2-D list
        cd = {}                                 # initialise new dictionary to store the elements are their occurances
        for num in nums:                        # store numbers as keys and their occurances as values
            if num in cd:
                cd[num] += 1
            else:
                cd[num] = 1
        maxValue = max(cd.values())             # calculate max times a number is in the list
        for i in range(0, maxValue):            # iterate max values times because that many time a number is in the list and we need that many seperate lists
            tempList = []                       # initialise temporary list to store the list with unique numbers
            for j, k in cd.items():             # iterate over the dictionary
                if k > 0:                       # check if current occurance of a number is greater than 0
                    tempList.append(j)          # add that number to the temporary list
                    cd[j] = k - 1               # decrement the value of the number
            newList.append(tempList)            # after reaching the end of the dictionary in each iteration append the temporary list to the new list
        return newList                          # return new list

mySol = Solution()
nums = [1,3,4,1,2,3,1]
print(mySol.findMatrix(nums))