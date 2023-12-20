#User function Template for python3
from collections import Counter
class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        # Your Code Here
        d=Counter(A1)
        res = []
        for i in A2:
            res.extend([i]*d[i])
            d[i]=0
        for i in sorted(d.keys()):
            while d[i]>0:
                res.append(i)
                d[i]-=1
        return res
                
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends