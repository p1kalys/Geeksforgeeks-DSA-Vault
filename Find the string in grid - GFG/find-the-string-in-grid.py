#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
		# Code here
		rows=len(grid)
		cols=len(grid[0])
		res=[]
		
		dx=[-1,1,0,0,-1,-1,1,1]
		dy=[0,0,-1,1,-1,1,-1,1]
		def valid(r,c,p):
		    if (r<0 or c<0 or r>=rows or c>=cols):
                return False
            return grid[r][c]==word[p]
		
		def dfs(x,y,d,p):
		    if p == len(word)-1:
		        return True
		    if valid(x+dx[d],y+dy[d],p+1):
		        return dfs(x+dx[d],y+dy[d],d,p+1)
            return False
            
		
		for i in range(rows):
		    for j in range(cols):
		        for k in range(8):
		            if valid(i,j,0) and dfs(i,j,k,0):
		                res.append([i,j])
		                break
        res.sort()
        
	    return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends