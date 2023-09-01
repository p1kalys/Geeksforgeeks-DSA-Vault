#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        i=0
        j=0
        s1=0
        ans=[-1]
        while j<n:
            s1+=arr[j]
            if s1==s:
                ans = [i+1,j+1]
                break
            elif s1>s:
                while s1>s and j>i:
                    s1-=arr[i]
                    i+=1
                    if s1==s:
                        ans=[i+1,j+1]
                        return ans
            j+=1
        return ans
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends