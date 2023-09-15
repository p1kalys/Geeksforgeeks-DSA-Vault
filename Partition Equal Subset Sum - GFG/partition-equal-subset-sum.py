# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        s=0
        for i in arr:
            s+=i
        if s%2!=0:
            return 'NO'
        
        s=s//2
        dp=[0]*(s+1)
        dp[0]=1
        for i in range(N):
            for j in range(s,arr[i]-1,-1):
                dp[j]|=dp[j-arr[i]]
        return dp[s]
        

#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends