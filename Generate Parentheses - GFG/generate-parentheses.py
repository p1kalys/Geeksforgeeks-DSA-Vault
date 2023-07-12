#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        self.ans = []
        s = ""
        self.generate(s, n, n)
        return self.ans

    def generate(self, s, o, c):
        if o == 0 and c == 0:
            self.ans.append(s)
            return
        if o > 0:
            s += '('
            self.generate(s, o - 1, c)
            s = s[:-1]
        if c > 0:
            if o < c:
                s += ')'
                self.generate(s, o, c - 1)
                s = s[:-1]




#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends