'''Given an array arr[] and an integer k, where the array represents the boards and each element denotes the length of a board, and k painters are available to paint these boards. Each unit length of a board takes 1 unit of time to paint. Find the minimum time required to paint all the boards such that each painter paints only contiguous sections of the array. A painter can paint boards like [2, 3, 4], [1], or even no board, but cannot paint non-contiguous boards like [2, 4, 5].'''

class Solution:
    def minTime (self, arr, k):
        low = max(arr)                              # Minimum feasible max time per painter.
        high = sum(arr)                             # Maximum time if one painter paints all boards.
        ans = -1                                    # Stores best feasible answer found so far.
        while low <= high:                          # Binary search over possible maximum times.
            mid = high + (low - high) // 2          # Candidate max time per painter.
            if self.isPossible(arr, k, mid):        # If feasible, try to minimize further.
                ans = mid                           # Update current best answer.
                high = mid - 1                      # Search left half for smaller feasible value.
            else:                                   # If not feasible, increase allowed time.
                low = mid + 1                       # Search right half.
        return ans                                  # Minimum time to paint all boards.

    def isPossible(self, arr, k, maxAllowedTime): # O(n)
        painter = 1                                  # Start with first painter.
        time = 0                                     # Current time assigned to this painter.
        for i in range(0, len(arr)):                 # Process boards in contiguous order.
            if time + arr[i] <= maxAllowedTime:      # Keep assigning if within limit.
                time += arr[i]                       # Add board length to current painter.
            else:                                    # Otherwise assign to next painter.
                painter += 1                         # Increase painter count.
                time = arr[i]                        # New painter starts with current board.
        if painter <= k:                             # Feasible if painters used are within k.
            return True                              # Allocation possible for this limit.
        else:                                        # More than k painters needed.
            return False                             # Allocation not possible.


mySol = Solution()                                   # Create solution object.
arr = [40, 30, 10, 20]                              # Input board lengths.
k = 2                                                # Total available painters.
print(mySol.minTime(arr, k))                        # Expected output: 60.