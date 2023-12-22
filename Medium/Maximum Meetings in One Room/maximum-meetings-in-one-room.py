from typing import List


class Solution:
    def maxMeetings(self, n : int, start : List[int], end : List[int]) -> List[int]:
        # code here
        mp=[]
        for i in range(n):
            mp.append([end[i],start[i],i+1])

        mp.sort(key=lambda x:x[0])
        cur=mp[0][0]
        res=[]
        res.append(mp[0][2])
        for i in range(n):
            if cur<mp[i][1]:
                cur=mp[i][0]
                res.append(mp[i][2])
        res.sort()
        return res


        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends