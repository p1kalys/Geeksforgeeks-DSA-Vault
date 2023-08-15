# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        ans=""
        temp=""
        for i in range(len(S)-1,-1,-1):
            if S[i]==".":
                ans+=temp[::-1]
                ans+="."
                temp=""
            else:
                temp+=S[i]
        ans+=temp[::-1]
        return ans


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends