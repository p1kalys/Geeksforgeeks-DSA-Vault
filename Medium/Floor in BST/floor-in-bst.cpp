//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

struct Node {
    int data;
    Node *right;
    Node *left;

    Node(int x) {
        data = x;
        right = NULL;
        left = NULL;
    }
};


// } Driver Code Ends
// Function to search a node in BST.
class Solution{

public:
    int floor(Node* root, int x) {
         if(!root) return 0;
        int temp = -1;
        //solve(root, x , temp);
        solveBST(root, x , temp);
        //if(temp > x) return -1;
        
        return temp;
    }
    
    void solve(Node* root, int x, int& temp){
        if(!root) return;
        if(root->data <= x && root->data >= temp) temp = root->data;
        
        solve(root->left, x, temp);
        solve(root->right, x, temp);
        return;
    }
    void solveBST(Node* root, int x, int& temp){
        if(!root) return;
        if(root->data <= x && root->data >= temp) temp = root->data;
        
        if(root->left && root->data > x) solveBST(root->left, x, temp);
        if(root->right && root->data < x) solveBST(root->right, x, temp);
        return;
    }
};

//{ Driver Code Starts.

Node *insert(Node *tree, int val) {
    Node *temp = NULL;
    if (tree == NULL) return new Node(val);

    if (val < tree->data) {
        tree->left = insert(tree->left, val);
    } else if (val > tree->data) {
        tree->right = insert(tree->right, val);
    }

    return tree;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        Node *root = NULL;

        int N;
        cin >> N;
        for (int i = 0; i < N; i++) {
            int k;
            cin >> k;
            root = insert(root, k);
        }

        int s;
        cin >> s;
        Solution obj;
        cout << obj.floor(root, s) << "\n";
    }
}

// } Driver Code Ends