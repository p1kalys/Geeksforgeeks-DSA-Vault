#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, N, ratings):
        # Code here
        candy = [1]*N
        for i in range(1,N):
            if ratings[i]>ratings[i-1]:
                candy[i] = candy[i-1]+1
        for i in range(N-1,0,-1):
            if ratings[i-1]>ratings[i] and candy[i-1]<=candy[i]:
                candy[i-1]=candy[i]+1
        return sum(candy)
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
# } Driver Code Ends