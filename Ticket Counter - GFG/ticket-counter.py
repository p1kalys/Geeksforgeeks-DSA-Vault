from collections import deque
class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        # Code Here
        q=deque()
        for i in range(1,N+1):
            q.append(i)
        flag=True
        while q:
            for j in range(K):
                ans=q[-1]
                if flag==True:
                    q.popleft()
                else:
                    q.pop()
                if len(q)==0:
                    break
                
            flag = not flag
        return ans

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends