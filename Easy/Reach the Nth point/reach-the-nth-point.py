#User function Template for python3

class Solution:
	def nthPoint(self,n):
		MOD = 10**9 + 7
		if n==1:
		    return 1
		elif n==2:
		    return 2
		    
		prev = 1
		ret = 2
		for i in range(2,n):
		    temp = ret+prev
		    prev = ret
		    ret = temp%MOD
		return temp%MOD


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends