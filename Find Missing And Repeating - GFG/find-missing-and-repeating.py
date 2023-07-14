#User function Template for python3

class Solution:
    def findTwoElement( self,a, n): 
        # code here
        n = len(a)  # size of the array

        # Find Sn and S2n:
        SN = (n * (n + 1)) // 2
        S2N = (n * (n + 1) * (2 * n + 1)) // 6
    
        # Calculate S and S2:
        S, S2 = 0, 0
        for i in range(n):
            S += a[i]
            S2 += a[i] * a[i]
    
        # S-Sn = X-Y:
        val1 = S - SN
    
        # S2-S2n = X^2-Y^2:
        val2 = S2 - S2N
    
        # Find X+Y = (X^2-Y^2)/(X-Y):
        val2 = val2 // val1
    
        # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
        # Here, X-Y = val1 and X+Y = val2:
        x = (val1 + val2) // 2
        y = x - val1
    
        return [x, y]


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