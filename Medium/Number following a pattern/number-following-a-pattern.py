#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        t = []
        res=""
        for i in range(len(S)+1):
            t.append(i+1)
            if (i==len(S) or S[i]=="I"):
                while (len(t)>0):
                    res+=str(t[-1])
                    t.pop()

        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends