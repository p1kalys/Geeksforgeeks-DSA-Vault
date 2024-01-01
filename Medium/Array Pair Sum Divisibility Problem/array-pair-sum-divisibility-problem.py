#User function Template for python3
import collections
class Solution:
	def canPair(self, nums, k):
		# Code here
		if len(nums)%2!=0:
		    return False
        d = [0]*k
		for i in nums:
		    x = i%k
		    if d[(k-x)%k]!=0:
		        d[(k-x)%k]-=1
		    else:
		        d[x]+=1
		        
		res = sum(d)
		if res>0:
		    return False
	    
	    return True
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends