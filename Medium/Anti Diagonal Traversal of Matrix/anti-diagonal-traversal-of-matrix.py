#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        n=len(matrix)
        ans = [0]*(n*n)
        s = 0
        k = 0
        while s!=2*n-1:
            i=0
            j=s
            if s>n-1:
                i=s-n+1
                j=n-1
            while i<= n-1 and j>=0:
                ans[k] = matrix[i][j]
                k+=1
                i+=1
                j-=1
            s+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends