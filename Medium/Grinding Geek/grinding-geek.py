
from typing import List

import math
class Solution:
    def f(self, ind, total,cost,dp):
        if ind >= len(cost):
            return 0
        if total==0:
            return 0
        if dp[ind][total]!=-1:
            return dp[ind][total]
        take = 0
        ref_cost = math.floor(90 * cost[ind]/100)
        if total >= cost[ind]:
            take = 1+self.f(ind+1,total + ref_cost - cost[ind], cost,dp)
        notake = self.f(ind+1,total,cost,dp)
        dp[ind][total] = max(take,notake)
        return dp[ind][total]
    
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        # code here
        dp = [[-1]*(total+1) for _ in range(n+1)]
        return self.f(0,total,cost,dp)
        



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
        
        n = int(input())
        
        
        total = int(input())
        
        
        cost=IntArray().Input(n)
        
        obj = Solution()
        res = obj.max_courses(n, total, cost)
        
        print(res)
        

# } Driver Code Ends