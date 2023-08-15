#User function Template for python3

class Solution:
    def minimumDays(self, S, N, M):
        # code here
        sun=S//7
        buy_days=S-sun
        totalFood=S*M
        if totalFood%N==0:
            ans=totalFood//N
        else:
            ans=totalFood//N + 1
        
        
        if ans<=buy_days:
            return ans
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, M = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.minimumDays(S, N, M))
# } Driver Code Ends