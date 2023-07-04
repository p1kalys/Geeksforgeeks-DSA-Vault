#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        p = 1
        res = 0
        start = 0
        end = 0
        while(end < n):
            # Move right bound by 1
            #Update the product.
            p *= a[end]
     
            # Move left bound  p is less than k.
            while (start < end and p >= k):
                p = int(p//a[start])
                start += 1
     
            # If p is less than k, update
            # the counter. Note that this
            # is working even for (start == end):
            # it means that the previous
            # window cannot grow anymore
            # and a single array element
            # is the only addendum.
            if (p < k):
                l = end - start + 1
                res += l
     
            end += 1
     
        return res
        
    
    
    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends