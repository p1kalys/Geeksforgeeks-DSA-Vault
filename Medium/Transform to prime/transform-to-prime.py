#User function Template for python3



class Solution:
    def isprime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
    
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    
    def f(self, n):
        if n <= 2:
            return 2
    
        prime = n
        while True:
            if self.isprime(prime):
                return prime
            prime += 1

    def minNumber(self, arr,n):
        temp = sum(arr)
        if self.isprime(temp):
            return 0
        else:
            res = self.f(temp)
            return res-temp



#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends