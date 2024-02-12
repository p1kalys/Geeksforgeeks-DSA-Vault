#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        if n<=1:
            return 1
        
        f = 0
        temp = 1
        MOD = 10**9 + 7
        for i in range(1,n+1):
            prod = 1
            j = 1
            while j <= i:
                prod *= temp
                prod%=MOD
                j+=1
                temp+=1
            f+=prod
            f %= MOD
        return f
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends