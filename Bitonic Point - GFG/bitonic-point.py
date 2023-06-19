#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		# code here
		left=0
		right=n-1
		while left!=right:
		    if arr[left]<arr[left+1]:
		        left+=1
	        if arr[right-1]>arr[right]:
	            right-=1
		return arr[left]


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends