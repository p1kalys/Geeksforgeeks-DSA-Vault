#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		i=0
		j=n-1
		while(i<=j):
		    m=i+(j-i)//2
		    if arr[m]==k:
		        return m
		    elif arr[m]>k:
		        j=m-1
	        else:
	            i=m+1
        return -1   


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends