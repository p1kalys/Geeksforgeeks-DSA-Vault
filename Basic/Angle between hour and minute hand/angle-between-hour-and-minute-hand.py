#User function Template for python3

class Solution:
    def getAngle(self, h , m):
        # code here
        if (h == 12):
            h = 0
        if (m == 60):
            m = 0
            h += 1;
            if(h>12):
                   h = h-12;
         
        # Calculate the angles moved by
        # hour and minute hands with
        # reference to 12:00
        hour_angle = 0.5 * (h * 60 + m)
        minute_angle = 6 * m
         
        # Find the difference between two angles
        angle = abs(hour_angle - minute_angle)
         
        # Return the smaller angle of two
        # possible angles
        angle = min(360 - angle, angle)
        return int(angle)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        H,M=map(int,input().split())
        
        ob = Solution()
        print(ob.getAngle(H,M))
# } Driver Code Ends