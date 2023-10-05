#User function Template for python3

class Solution:
    def f(self, s, k):
        d = {}
        count = 0
        l = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            
            while len(d) > k :
                if d[s[l]] == 1:
                    del d[s[l]]
                else:
                    d[s[l]] -= 1
                l+=1
            count += i-l+1
        return count
    
    def substrCount (self,s, k):
        return self.f(s, k) - self.f(s, k-1)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends