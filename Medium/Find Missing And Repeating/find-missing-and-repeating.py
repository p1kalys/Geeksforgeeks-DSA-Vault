#User function Template for python3

class Solution:
    def findTwoElement( self,A, n):
        length = len(A)
        Sum_N = (length * (length + 1)) // 2
        Sum_NSq = ((length * (length + 1) *
                         (2 * length + 1)) // 6)
         
        missingNumber, repeating = 0, 0
         
        for i in range(len(A)):
            Sum_N -= A[i]
            Sum_NSq -= A[i] * A[i]
             
        missingNumber = (Sum_N + Sum_NSq //
                                 Sum_N) // 2
        repeating = missingNumber - Sum_N
         
        ans = []
        ans.append(repeating)
        ans.append(missingNumber)
         
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends