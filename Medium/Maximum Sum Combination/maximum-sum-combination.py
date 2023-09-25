#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import heapq
class Solution:
    def maxCombinations(self, n, k, arr, brr):
        # Code here
        arr = sorted(arr, reverse = True)
        brr = sorted(brr, reverse = True)
        
        ans = []
        l = []
        
        for i in range(n):
            heapq.heappush(l, (-(arr[i]+brr[0]), 0))
        
        while k:
            # print(l)
            curr = heapq.heappop(l)
            ans.append(-curr[0])
            
            if curr[1] < n-1:
                ind = -(-curr[0]-brr[curr[1]]+brr[curr[1]+1])
                heapq.heappush(l, (ind, curr[1]+1))
            k -= 1
        
        return ans  

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxCombinations(N, K, A, B)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends