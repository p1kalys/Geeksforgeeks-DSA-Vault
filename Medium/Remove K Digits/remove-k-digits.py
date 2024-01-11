#User function Template for python3

class Solution:

    def removeKdigits(self, S, K):
        stack = []

        for digit in S:
            # Remove elements from the stack until a smaller element or k removals are done
            while K > 0 and stack and stack[-1] > digit:
                stack.pop()
                K -= 1

            # Push the current digit onto the stack
            stack.append(digit)

        # Remove remaining elements if needed
        while K > 0:
            stack.pop()
            K -= 1

        # Construct the result string
        result = ''.join(stack).lstrip('0')

        # If the result is empty, return '0'
        return result if result else '0'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends