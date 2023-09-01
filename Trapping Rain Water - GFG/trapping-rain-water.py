
class Solution:
    def trappingWater(self, arr,n):
        l=0
        r=n-1
        ml=0
        mr=0
        s=0
        while l<=r:
            if arr[l]<=arr[r]:
                if arr[l]>ml:
                    ml=arr[l]
                else:
                    s+=ml-arr[l]
                l+=1
            else:
                if arr[r]>mr:
                    mr=arr[r]
                else:
                    s+=mr-arr[r]
                r-=1
        return s    
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends