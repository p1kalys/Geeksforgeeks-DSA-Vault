#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def betterString(self, str1, str2):
        def f(s):
            l = {}
            count = 1
            for c in s:
                new = 2*count
                if c in l:
                    new -= l[c]
                l[c] = count
                count = new
            return count
        d1 = f(str1)
        d2 = f(str2)
        
        if d2 > d1:
            return str2
            
        else: 
            return str1
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends