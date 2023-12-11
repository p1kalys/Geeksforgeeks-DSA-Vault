#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        cur = sum(Arr[:K])
        res = cur
        for i in range(K,N):
            cur = cur - Arr[i-K] + Arr[i]
            res = max(res,cur)
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends