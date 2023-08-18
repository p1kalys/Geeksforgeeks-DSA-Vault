#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        i=0
        j=0
        count=0
        while i<n and j<m:
            if arr1[i]<arr2[j]:
                count+=1
                i+=1
                if k==count:
                    return arr1[i-1]
            else:
                count+=1
                j+=1
                if k==count:
                    return arr2[j-1]
        while i<n:
            count+=1
            i+=1
            if k==count:
                return arr1[i-1]  
        while j<m:
            count+=1
            j+=1
            if k==count:
                return arr2[j-1]  
            
                
                    
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends