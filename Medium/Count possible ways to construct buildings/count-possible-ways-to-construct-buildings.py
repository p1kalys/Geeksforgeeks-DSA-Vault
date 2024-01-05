#User function Template for python3

class Solution:
	def TotalWays(self, N):
	    MOD = 10**9+7
		dp=[-1]*(N+1)
		dp[0] = 1
		dp[1]=2
		for i in range(2,N+1):
		    dp[i] = (dp[i-1]%MOD + dp[i-2]%MOD)%MOD
		return (dp[N]*dp[N])%MOD


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends