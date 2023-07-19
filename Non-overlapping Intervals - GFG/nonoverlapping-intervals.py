#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, N, intervals):
        # Code here
        intervals.sort(key=lambda x:x[1])
        count=1
        j=0
        for i in range(1,N):
            if intervals[i][0]>=intervals[j][1]:
                j=i
                count+=1
        return N-count

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(N, intervals)
        print(res)
# } Driver Code Ends