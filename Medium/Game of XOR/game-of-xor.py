#User function Template for python3

class Solution:
    def gameOfXor(self, N , A):
        # code here 
        x = 0
        for i in range(N):
            fre = (i+1) * (N-i)
            if fre%2 == 1:
                x^=A[i]
        return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.gameOfXor(N,A))
# } Driver Code Ends