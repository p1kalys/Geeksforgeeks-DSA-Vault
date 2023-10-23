#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
	    dp = [0]*n
		dp[0] = Arr[0]
		for i in range(n):
	        for j in range(i):
                if (Arr[j]<Arr[i]):
                    dp[i]=max(dp[i], Arr[i]+dp[j])
                else:
                    dp[i]=max(dp[i],Arr[i])
        return max(dp)
		      
		       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends