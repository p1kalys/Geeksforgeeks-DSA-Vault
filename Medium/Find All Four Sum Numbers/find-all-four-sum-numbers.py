#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        s=0
        res=set()
        arr.sort()
        for i in range(len(arr)-3):
            for j in range(i+1,len(arr)-2):
                r=j+1
                l=len(arr)-1
                while r<l:
                    s=arr[i]+arr[j]+arr[r]+arr[l]
                    if s==k:
                        res.add((arr[i],arr[j],arr[r],arr[l]))
                        r+=1
                    elif s<k:
                        r+=1
                    else:
                        l-=1
        res_list = sorted(list(res))
        return res_list


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends