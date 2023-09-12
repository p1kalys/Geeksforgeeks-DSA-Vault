#User function Template for python3
import math
class Solution:
    def isPerfectNumber(self, N):
        # code here 
        if N==1:
            return 0
        sum=1
        i=2
        while  i <= math.sqrt(N):
            if N%i==0:
                sum+=i
                sum+=(N//i)
            i+=1
        if sum==N:
            return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends