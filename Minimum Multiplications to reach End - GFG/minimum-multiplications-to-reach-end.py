#User function Template for python3
from collections import deque
from typing import List

class Solution:
    
    def minimumMultiplications(self, multipliers : List[int], start_value : int, target_value : int) -> int:
        # code here
        max_mod_value = 100000  # Maximum mod value
        queue = deque()  # Use a queue for breadth-first search
        
        min_steps_to_value = [-1 for _ in range(max_mod_value)]  # Store minimum steps to reach each value
        start_mod_value = start_value % max_mod_value  # Calculate the modulo of the start value
        
        queue.append([start_mod_value, 0])  # Initialize the queue with the start value and step count
        min_steps_to_value[start_mod_value] = 0  # Mark the start value with 0 steps

        while queue:
            current_value, steps = queue.popleft()  # Dequeue the current value and step count

            if current_value == target_value:
                return min_steps_to_value[target_value]  # If the target value is reached, return the steps

            for multiplier in multipliers:
                next_value = (current_value * multiplier) % max_mod_value  # Calculate the next value
                
                if min_steps_to_value[next_value] == -1:
                    queue.append([next_value, steps + 1])  # Enqueue the next value and increment the steps
                    min_steps_to_value[next_value] = steps + 1  # Update the steps to reach the next value

        return -1  # If the target value cannot be reached, return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends