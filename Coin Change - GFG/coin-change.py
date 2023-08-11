#User function Template for python3

class Solution:
    def count(self, S, m, n): 
        size = m
        arr = [[0] * (n + 1) for x in range(size + 1)]
        
        for i in range(size + 1):
            arr[i][0] = 1
        
        for i in range(1, size + 1):
            for j in range(1, n + 1):
                if S[i - 1] > j:  
                    arr[i][j] = arr[i - 1][j]
                else: 
                    arr[i][j] = arr[i - 1][j] + arr[i][j - S[i - 1]]
        
        return arr[size][n]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends