'''Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
All books must be allocated.
The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: If it is not possible to allocate books to all students, return -1.'''


class Solution:
    def findPages(self, arr, k):                     # O(nlogn)
        n = len(arr)                                 # Total number of books.
        if k > n:                                    # Impossible if students exceed books.
            return -1                                # Return failure as per problem statement.
        start = 0                                    # Lower bound for maximum pages.
        end = sum(arr)                               # Upper bound if one student gets all books.
        ans = -1                                     # Stores best feasible maximum pages.
        while start <= end:                          # Binary search on answer space.
            mid = start + (end - start) // 2         # Candidate maximum pages per student.
            if self.isValid(arr, k, n, mid):         # Check if this candidate is feasible.
                ans = mid                            # Record feasible answer.
                end = mid - 1                        # Try to minimize the maximum pages.
            else:                                    # Candidate too small to allocate all books.
                start = mid + 1                      # Increase lower bound.
        return ans                                   # Minimum possible maximum pages.
    
    def isValid(self, arr, m, n, maxAllowedPages):   # O(n)
        students = 1                                 # Start allocation with first student.
        pages = 0                                    # Pages currently assigned to this student.
        for i in range(0, n):                        # Traverse books in order (contiguous rule).
            if arr[i] > maxAllowedPages:             # Single book exceeds candidate limit.
                return False                         # Candidate is impossible.
            if pages + arr[i] <= maxAllowedPages:    # Add current book if limit not exceeded.
                pages += arr[i]                      # Continue assigning to same student.
            else:                                    # Need another student for this book.
                students += 1                        # Increment student count.
                pages = arr[i]                       # Start new student's allocation.
        if students > m:                             # Used more students than allowed.
            return False                             # Candidate is not feasible.
        else:                                        # Student usage is within limit.
            return True                              # Candidate is feasible.


mySol = Solution()                                   # Create solution object.
arr = [12, 34, 67, 90]                               # Input pages per book.
k = 2                                                # Number of students.
print(mySol.findPages(arr, k))                       # Expected output: 113.