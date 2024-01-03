#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        ans = len(S) + 1
        left, right = 0, 0
        hmap = {"0": 0, "1": 0, "2": 0}
        while right < len(S):
            hmap[S[right]] += 1
            while hmap["0"] and hmap["1"] and hmap["2"]:
                ans = min(ans, right - left + 1)
                hmap[S[left]] -= 1
                left += 1
            right += 1
        return ans if ans <= len(S) else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends