
from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        # code here
        ans,flag,buy = 0, 0, 10 ** 10
        if len(prices) <= 1:
            return 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                if not flag:
                    flag = 1
                    buy = prices[i]
            else:
                if flag:
                    flag = 0
                    ans += prices[i] - buy
                    buy = 10 **  10
        ans += (prices[i + 1] - buy > 0) * (prices[i + 1] - buy)
        return ans
        



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
        
        
        prices=IntArray().Input(n)
        
        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)
        
        print(res)
        

# } Driver Code Ends