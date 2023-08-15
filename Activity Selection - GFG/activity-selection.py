#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        d=[]
        for i in range(n):
            d.append([end[i],start[i]])
        d.sort(key=lambda x:x[0])
        res=1
        cur=d[0][0]
        for i in range(1,n):
            if cur<d[i][1]:
                cur=d[i][0]
                res+=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends