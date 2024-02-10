#User function Template for python3

class Solution:
    def f(self, arr, i,j, k, dp, n):
        if i == n-1 and j==n-1:
            return 1 if k==arr[i][j] else 0 
        if i<0 or j<0 or i >=n or j>=n or k<0:
            return 0
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        dp[i][j][k] = self.f(arr,i,j+1,k-arr[i][j],dp,n) + self.f(arr, i+1,j,k-arr[i][j], dp,n)
        return dp[i][j][k]
            
    
    def numberOfPath (self, n, k, arr):
        # code here
        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(n)]
        
        return self.f(arr, 0, 0, k, dp, n)




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        k= int(input())
        n=int(input())
        l = list(map(int, input().split()))
        arr = list()
        c=0
        for i in range(0, n):
            temp = list()
            for j in range(0, n):
                temp.append(l[c])
                c += 1
            arr.append(temp)
        ans = ob.numberOfPath(n, k, arr);
        print(ans)


# } Driver Code Ends