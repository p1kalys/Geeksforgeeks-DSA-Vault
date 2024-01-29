#User function Template for python3

class Solution:
	def TotalCount(self, s):
		# Code here
		n = len(s)
		
		dp = {}
		def f(i,temp):
		    if i>=n:
		        return 1

		    if (i,temp) in dp:
		        return dp[(i,temp)]

		    ns = 0
		    res = 0
		    for j in range(i,n):
		        ns += int(s[j])
		        if ns >= temp:
		            res += f(j+1,ns)
	        dp[(i,temp)] = res
	        return dp[(i,temp)]
	    return f(0,0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends