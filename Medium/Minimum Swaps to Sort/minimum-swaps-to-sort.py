

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		d=[]
		for i in range(len(nums)):
		    d.append([nums[i],i])
		d.sort()
		res=0
		i=0
		while i < len(nums):
		    if d[i][1]!=i:
		        res+=1
		        d[d[i][1]],d[i] = d[i], d[d[i][1]]
		        continue
		    i+=1
		return res
		        


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends