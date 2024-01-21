from typing import List


class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        # code here
        def compute(edges, s=set()):
            if not edges:
                return len(s)
            u, v = edges.pop()
            if u in s or v in s:
                return compute(edges, s)
            
            c1 = compute(edges[:], s.union({u}))
            c2 = compute(edges, s.union({v}))
            return min(c1, c2)
        
        return compute(edges)
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        
        edges=IntMatrix().Input(m, m)
        
        obj = Solution()
        res = obj.vertexCover(n, edges)
        
        print(res)
        

# } Driver Code Ends