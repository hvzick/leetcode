'''There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.'''

class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        hashMap = {}                                    # initialise empty dictionary
        c = []                                          # initialise empty list
        temp = []                                       # initialise empty list
        for i in range(0, len(groupSizes)):
            if groupSizes[i] not in hashMap:            # if key is not present
                hashMap[groupSizes[i]] = []             # add the key its value
                hashMap[groupSizes[i]].append(i)        # append current index to the value
            else:
                hashMap[groupSizes[i]].append(i)        # if key is present add current index to the list of values
        for key, value in hashMap.items():              # iterate over the hash map
            for i in value:                             # iterate over the list of values
                if len(temp) < key:                     # if size of list is less than key
                    temp.append(i)                      # append current index to the key
                if len(temp) == key:                    # when size reaches the size of groups(key)
                    c.append(temp)                      # add the list to another list
                    temp = []                           # reset the temporary list
        return c                                        # return the list

mySol = Solution()
groupSizes = [3,3,3,3,3,1,3]
print(mySol.groupThePeople(groupSizes))