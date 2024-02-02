#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        num = 0
        sign = 1
        i = 0
        if s[0]=='-':
            sign = -1
            i+=1
        while i<len(s):
            if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                num = num*10 + ord(s[i]) - ord('0')
            else:
                return -1
            i+=1
        return sign * num


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends