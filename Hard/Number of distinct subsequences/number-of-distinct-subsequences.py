#User function Template for python3

class Solution:
	def distinctSubsequences(self, S):
		# code here
		n=len(S)
		mod=10**9 + 7
		f=[-1]*26
		dp=[0]*(n+1)
		dp[0]=1
		for i in range(1,n+1):
		    dp[i] = dp[i-1]*2
		    last_element = f[ord(S[i-1])-ord('a')]
		    if last_element!=-1:
		        dp[i] -= dp[last_element]
		        if dp[i]<0:
		            dp[i]+=mod
		    dp[i]%=mod
		    f[ord(S[i-1])-ord('a')]=i-1
	    return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends