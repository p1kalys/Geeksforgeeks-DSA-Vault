#User function Template for python3

class Solution:
    def countSubarrays(self, a,n,L,R): 
        # Complete the function
        i=0
        res=0
        rang=0
        for j in range(n):
            if a[j]>=L and a[j]<=R:
                rang = j-i+1
            elif a[j]>r:
                rang = 0
                i=j+1
            res+=rang
        return res
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    n,l,r = map(int, input().strip().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    v = ob.countSubarrays(arr, n, l, r)
    print(v)
    
# } Driver Code Ends