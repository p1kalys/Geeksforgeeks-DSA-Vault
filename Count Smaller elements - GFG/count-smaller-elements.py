#User function Template for python3
from bisect import bisect_left
class Solution:

	def constructLowerArray(self,arr, n):
		# code here
		ans=[]
		vs=sorted(arr)
		for i in range(len(arr)):
            index = bisect_left(vs, arr[i])
            ans.append(index)
            del vs[index]
    
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends