#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        s=n*(n+1)//2
        s1=n*(n+1)*(2*n + 1)//6
        sn=0
        s1n=0
        for i in range(n):
            sn+=arr[i]
            s1n+=(arr[i]**2)
        val1=sn-s
        val2=s1n-s1
        val2=val2//val1
        x=(val1+val2)//2
        y=x-val1
        return [x,y]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends