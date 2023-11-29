class Solution:
	def isEulerCircuitExist(self, V, adj):
		#Code here
		odd = 0
		even = 0
		for i in range(V):
		    if len(adj[i])%2==0:
		        even += 1
		    else:
		        odd += 1
        if even == V:
            return 2
        elif odd > 0 and odd ==2:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEulerCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends