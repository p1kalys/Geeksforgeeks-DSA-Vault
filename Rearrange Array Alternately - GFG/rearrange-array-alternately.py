#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        i=0
        j=0
        k=n-1
        key=arr[-1]+1
        while i<n:
            if i%2==0:
                arr[i]=(arr[k]%key)*key + arr[i]
                k-=1
            else:
                arr[i]=(arr[j]%key)*key + arr[i]
                j+=1
            i+=1
        for i in range(n):
            arr[i]=arr[i]//key

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends