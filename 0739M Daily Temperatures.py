'''Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.'''

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n =len(temperatures)
        answers = [0] * n                               # initialise an array with zeroes of lenght temperatures
        stack = []                                      # initialise a stack
        stack.append(0)                                 # because its empty
        for today in range(1, n):                       # loop over the temperatures
            while stack and temperatures[today] > temperatures[stack[-1]]:  # check if stack is empty and temperature of today is > temperature of yesterday at top of the stack
                yesterday = stack.pop()                 # pop the top of the stack
                answers[yesterday] = today - yesterday  # add the day difference of today and yesterday to answers array at yesterdays index
            stack.append(today)                         # if stack is empty append or if temperature of today < temperature of yesterday append today to the stack
        return answers                                  # return the answers array

mySol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(mySol.dailyTemperatures(temperatures))
