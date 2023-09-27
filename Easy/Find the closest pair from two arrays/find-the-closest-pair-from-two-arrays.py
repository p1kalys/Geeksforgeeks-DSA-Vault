#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        #code here
        dif=float('inf')
        res=None
        i1 = 0
        i2 = m-1
        while i1 < n and i2>=0:
            s = arr[i1]+brr[i2]
            cur_dif = abs(s-x)
            if cur_dif < dif:
                res=[arr[i1],brr[i2]]
                dif = cur_dif
            if s<x:
                i1+=1
            else:
                i2-=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends