#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        rmap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"%":0}
        res=0
        n=len(S)
        
        # main loop
        for i in range(n):
            currch=S[i]
            if i<n-1:
                nextch=S[i+1]
            else:
                nextch="%"
            if rmap[currch]>=rmap[nextch]:
                res=res+rmap[currch]
            else:
                res=res-rmap[currch]
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends