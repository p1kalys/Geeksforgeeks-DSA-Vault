#User function Template for python3
import math
from math import gcd
class Solution:
    def countFractions(self, n, numerator, denominator):
        res={}
        ans=0
        # Your code here
        for i,j in zip(numerator,denominator):
            g=gcd(i,j)
            i//=g
            j//=g
            ans+=res.get((j-i,j),0)
            res[(i,j)]=res.get((i,j),0)+1
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    numerator = list(map(int,input().split()))
    denominator = list(map(int,input().split()))
    ob = Solution()
    print(ob.countFractions(n,numerator,denominator))
# } Driver Code Ends