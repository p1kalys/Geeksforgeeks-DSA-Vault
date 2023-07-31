#User function Template for python3

class Solution:
    def helper(self,i,j,m,n,slate,res):
        if(i<0 or i>=n or j<0 or j>=n or m[i][j]==0):
            return 
        if i==n-1 and j==n-1:
            res.append(slate)
            return
        m[i][j]=0
     
        self.helper(i+1,j,m,n,slate+'D',res)
       
        self.helper(i,j-1,m,n,slate+'L',res)
       
        self.helper(i,j+1,m,n,slate+'R',res)

        self.helper(i-1,j,m,n,slate+'U',res)
        m[i][j]=1
        return
        
    
    
    def findPath(self, m, n):
        # code here
        res=[]
        slate=""
        self.helper(0,0,m,n,slate,res)
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends