#User function Template for python3

class Solution:
    def rotateMatrix(self, M, N, Mat):
        #code here
        top = 0
        bottom = len(Mat)-1
     
        left = 0
        right = len(Mat[0])-1
     
        while left < right and top < bottom:
     
            # Store the first element of next row,
            # this element will replace first element of current row
            prev = Mat[top+1][left]
     
            # Move elements of top row one step right
            for i in range(left, right+1):
                curr = Mat[top][i]
                Mat[top][i] = prev
                prev = curr
     
            top += 1
     
            # Move elements of rightmost column one step downwards
            for i in range(top, bottom+1):
                curr = Mat[i][right]
                Mat[i][right] = prev
                prev = curr
     
            right -= 1
     
            # Move elements of bottom row one step left
            for i in range(right, left-1, -1):
                curr = Mat[bottom][i]
                Mat[bottom][i] = prev
                prev = curr
     
            bottom -= 1
     
            # Move elements of leftmost column one step upwards
            for i in range(bottom, top-1, -1):
                curr = Mat[i][left]
                Mat[i][left] = prev
                prev = curr
     
            left += 1
     
        return Mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        ans=ob.rotateMatrix(N,M,A)
        for i in range(N):
            for j in range(M):
                print(ans[i][j],end=" ")
            print()    
# } Driver Code Ends