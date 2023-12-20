# function to return maximum XOR subset in set[]

class Solution:
    def maxSubsetXOR(self, arr, N):
        # add code here
        arr.sort()
        res = 0
        while True:
            maxi = max(arr)
            if maxi==0:
                return res
            res = max(res, res ^ maxi)
            
            for i in range(N):
                arr[i] = min(arr[i],arr[i]^maxi)
        return res

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        set=list(map(int,input().split()))
        obj = Solution()
        print(obj.maxSubsetXOR(set,n))

# } Driver Code Ends