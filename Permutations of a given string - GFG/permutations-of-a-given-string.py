#User function Template for python3
from itertools import permutations
class Solution:
    def find_permutation(self, S):
        # Code here
        res=[]
        permut=permutations(S)
        for i in list(sorted(set(permut))):
            res.append(''.join(i))
        return res
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends