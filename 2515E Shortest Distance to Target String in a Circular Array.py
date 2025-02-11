'''You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.

Example 1:

Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1
Explanation: We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.'''

class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        if target not in words:                          # check if the word is present in  the list or no
            return -1
        elif words[startIndex] == target:                # check if the word is present at the current index so return 0 because we are not moving anywhere to reach the
            return 0
        shortest_distance = 10000                        # initialist it to lorger value to update it with smaller values
        longest_distance = 0                             # initialist it to smaller value to update it with larger values
        length = len(words)
        c1 = 0
        c2 = 0
        for i in range(startIndex, startIndex + length):
            index = i % length
            if words[index] == target and c1 <= shortest_distance: # if the word at current index is target word and c1 is the shortest distance then update the shortest_distance
                shortest_distance = c1
            if words[index] == target and c2 >= longest_distance: # if the word at current index is target word and c2 is the longest distance then update the longest_distance
                longest_distance = c2
            c1 += 1
            c2 += 1
        #print(shortest_distance, longest_distance)
        if length - longest_distance < shortest_distance: # check if its smaller than shortest_distance, if yes then it must be on the left side of the starting index
            return length - longest_distance              
        return shortest_distance

mySol = Solution()
words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1
print(mySol.closetTarget(words, target, startIndex))