#User function Template for python3

class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here
		i=0
		a1=0
		a2=0
		ele1 = 0
		ele2 = 0
		while i<=n and a1<len(ar1) and a2<len(ar2):
		    if ar1[a1]<ar2[a2]:
		        i+=1
		        temp = ar1[a1]
		        a1+=1
		    else:
		        
		        i+=1
		        temp=ar2[a2]
		        a2+=1
		    ele2 = ele1
		    ele1 = temp
		    
		while i<=n and a1<len(ar1):
		    i+=1
		    temp = ar1[a1]
		    a1+=1
		    ele2 = ele1
		    ele1 = temp
		    
		while i<=n and a2<len(ar2):
		    i+=1
		    temp = ar2[a2]
		    a2+=1
		    ele2 = ele1
		    ele1 = temp
	    return ele1+ele2
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1

# } Driver Code Ends