#User function Template for python3
class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, K):
        d = {}
        d[0]=-1
        cur_sum = 0
        ans = 0
        for i in range(n):
            cur_sum += arr[i]
            rem = cur_sum % K
            if rem < 0:
                rem += K
            
            if rem not in d.keys():
                d[rem] = i
            else:
                ans = max(ans, i - d[rem])
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends