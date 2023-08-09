#User function Template for python3
import math

class Solution:
    def largestPrimeFactor (self, N):
        # code here
        k=math.ceil(math.sqrt(N))
        ans=1
        for i in range(2,k+1):
            if N%i==0:
                ans=i
                while N%i==0:
                    N//=i
                
        return max(ans,N)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends