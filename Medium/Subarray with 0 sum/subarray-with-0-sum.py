#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        n_sum = 0
        s = set()
     
        for i in range(n):
            n_sum += arr[i]
     
            # If prefix sum is 0 or
            # it is already present
            if n_sum == 0 or n_sum in s:
                return True
            s.add(n_sum)
     
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends