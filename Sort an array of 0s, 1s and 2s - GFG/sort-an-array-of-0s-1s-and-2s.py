#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        lo=0
        mid=0
        hi=n-1
        while mid<=hi:
            if arr[mid]==0:
                arr[mid],arr[lo]=arr[lo],arr[mid]
                lo+=1
                mid+=1
            elif arr[mid]==2:
                arr[mid],arr[hi]=arr[hi],arr[mid]
                hi-=1
            else:
                mid+=1
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends