#User function Template for python3

class Solution:
    def kTop(self,a, N, K):
        #code here.
        res = []
        d={i:0 for i in range(K+1)}
        top = [0]*(K+1)
        for m in range(N):
            d[a[m]] = d.get(a[m],0)+1
            top[K] = a[m]
            i = top.index(a[m])
            i -= 1
            while i>=0:
                if d[top[i]] < d[top[i+1]]:
                    t = top[i]
                    top[i] = top[i+1]
                    top[i+1] = t
                elif d[top[i]] == d[top[i+1]] and top[i] > top[i+1]:
                    t = top[i]
                    top[i] = top[i+1]
                    top[i+1] = t
                else:
                    break
                i-=1
            i=0
            ans = []
            while i<K and top[i]!=0:
                ans.append(top[i])
                i+=1
            res += [ans]
        return res


#{ 
 # Driver Code Starts


t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.kTop(a,n,k)
    for line in ans:
        print(*line)



# } Driver Code Ends