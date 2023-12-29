#User function Template for python3
class Solution:
	def kSubstrConcat(self, n, s, k):
		# Your Code Here
		if n%k != 0:
		    return 0
		
		res = 0
		d = {}
		for i in range(0,n,k):
		    d[s[i:i+k]] = d.get(s[i:i+k],0)+1
		    
		if len(d)<=2:
		    return 1
		else:
		    return 0
		    
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends