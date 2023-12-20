#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        res = ""
        min_len = min(len(a) for a in arr)
        for i in range(min_len):
            ele = arr[0][i]
            for j in range(n):
                if ele!=arr[j][i]:
                    if len(res)==0:
                        return -1
                    return res
            res+=ele
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends