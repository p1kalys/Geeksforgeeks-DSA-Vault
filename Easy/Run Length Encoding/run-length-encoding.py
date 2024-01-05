#Your task is to complete this function
#Function should return complete string
def encode(arr):
    count = 1
    res = ""
    res+=arr[0]
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            res+=str(count)
            res+=arr[i]
            count = 1
    
    res+=str(count)
    return res

#{ 
 # Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends