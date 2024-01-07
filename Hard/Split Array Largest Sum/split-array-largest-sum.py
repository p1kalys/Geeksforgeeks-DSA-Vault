#User function Template for python3

class Solution:
    def splitArray(self, arr, N, K):
        l = max(arr)
        r = sum(arr)
        ans = 0
        
        def f(mid):
            total = 1
            s = 0
            for i in range(N):
                s+=arr[i]
                if s>mid:
                    s = arr[i]
                    total+=1
            return total <= K
            
        while l<=r:
            mid = (l+r)//2
            if f(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends