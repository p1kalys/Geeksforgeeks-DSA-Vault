#User function Template for python3

class Solution:
    def findString(self, n, k):
        ans=['0']*n
        temp=ans.copy()
        map={}
        map[''.join(temp)]=1
        self.dfs(temp,ans,map,k)
        return ''.join(ans)
    
    def dfs(self,curr,ans,map,k):
        temp=curr[1:]
        for i in range(k-1,-1,-1):
            temp.append(str(i))
            temp_str=''.join(temp)
            if temp_str not in map:
                map[temp_str]=1
                ans.append(str(i))
                self.dfs(temp,ans,map,k)
                return 
            temp.pop()
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())

        ob = Solution()
        ans = ob.findString(N,K)
        ok = 1
        for i in ans:
            if ord(i)<48 or ord(i)>K-1+48:
                ok = 0
        if not ok:
            print(-1)
            continue
        d = dict()
        i = 0
        while i+N-1<len(ans):
            d[ans[i:i+N]] = 1
            i += 1
        tot = pow(K,N)
        if len(d)==tot:
            print(len(ans))
        else:
            print(-1)
# } Driver Code Ends