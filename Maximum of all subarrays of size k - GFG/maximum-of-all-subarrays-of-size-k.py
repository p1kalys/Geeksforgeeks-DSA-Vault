#User function Template for python3
from collections import deque
class Solution: 

    def max_of_subarrays(self, arr, n, k):
        res = []
        q = deque()
    
        # Process the first k elements separately
        for i in range(k):
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
    
        # Process the remaining elements
        for i in range(k, n):
            res.append(arr[q[0]])
    
            # Remove elements that are out of the current window
            while q and q[0] <= i - k:
                q.popleft()
    
            # Remove elements smaller than the current element
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
    
            q.append(i)
    
        res.append(arr[q[0]])  # Append the maximum element of the last window
    
        return res
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends