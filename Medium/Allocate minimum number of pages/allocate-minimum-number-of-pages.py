class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if M>N:
            return -1
        s=max(A)
        e = sum(A)
        while s<=e:
            m=s+(e-s)//2
            page=0
            count=1
            for i in range(N):
                page+=A[i]
                if page>m:
                    count+=1
                    page=A[i]
            if count<=M:
                ans = m
                e = m-1
            else:
                s=m+1
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends