#User function Template for python3

class Solution:
	def Count(self, matrix):
		# Code here
		dx=[-1,1,0,0,-1,1,-1,1]
		dy=[0,0,1,-1,-1,-1,1,1]
		c=0
		n=len(matrix)
		m=len(matrix[0])
		
		def valid(x,y):
		    if (x<0 or x>=n or y<0 or y>=m):
		        return 0
		    if matrix[x][y]==0:
		        return 1
	        return 0
	        
	        
		for i in range(len(matrix)):
		    for j in range(len(matrix[i])):
		        if matrix[i][j]==0:
		            continue
		        else:
		            zeros=0
		            for k in range(8):
		                x=i+dx[k]
		                y=j+dy[k]
		                zeros += valid(x,y)
                    if zeros and zeros%2==0:
                        c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends