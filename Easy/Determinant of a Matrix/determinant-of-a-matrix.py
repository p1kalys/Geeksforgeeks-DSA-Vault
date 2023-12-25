
#User function Template for python3

class Solution:
    
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,matrix,n):
        # code here 
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0]* matrix[0][1]
        deter = 0
        for i in range(n):
            minor_mat = [row[:i] + row[i+1:] for row in matrix[1:]]
            cofac = matrix[0][i]*((-1) **i)
            deter += cofac*self.determinantOfMatrix(minor_mat, n-1)
        return deter


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends