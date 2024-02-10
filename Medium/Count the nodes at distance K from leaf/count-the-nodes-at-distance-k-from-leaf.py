#User function Template for python3

'''
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

from collections import deque

class Solution:
    def __init__(self):
        self.result = 0

    def printKDistantfromLeaf(self, root, k):
        queue = deque([(root, [], 0)])  # (node, path, distance)
        leaf_paths = []

        while queue:
            node, path, distance = queue.popleft()

            if not node.left and not node.right:
                leaf_paths.append((path + [node], distance + 1))
                continue

            if node.left:
                queue.append((node.left, path + [node], distance + 1))

            if node.right:
                queue.append((node.right, path + [node], distance + 1))

        return len(set([path[-k - 1] for path, distance in leaf_paths if distance - 1 >= k]))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

MAX_HEIGHT = 100000
c=0
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip=list(map(str,s.split()))

    # Create the root of the tree
    root=Node(int(ip[0]))
    size=0
    q=deque()

    # Push the root to the queue
    q.append(root)
    size=size+1

    # Starting from the second element
    i=1
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1

        # Get the current node's value from the string
        currVal=ip[i]

        # If the left child is not null
        if(currVal!="N"):

            # Create the left child for the current node
            currNode.left=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]

        # If the right child is not null
        if(currVal!="N"):

            # Create the right child for the current node
            currNode.right=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        k = int(input())
        ob = Solution()
        print(ob.printKDistantfromLeaf(root, k))

# } Driver Code Ends