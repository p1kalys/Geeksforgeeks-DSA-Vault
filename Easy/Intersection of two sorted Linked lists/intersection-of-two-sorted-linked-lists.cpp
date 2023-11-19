//{ Driver Code Starts
//

#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node(int val)
    {
        data=val;
        next=NULL;
    }
};

Node* inputList(int size)
{
    Node *head, *tail;
    int val;
    
    cin>>val;
    head = tail = new Node(val);
    
    while(--size)
    {
        cin>>val;
        tail->next = new Node(val);
        tail = tail->next;
    }
    
    return head;
}

void printList(Node* n)
{
    if(n)
    while(n)
    {
        cout<< n->data << " ";
        n = n->next;
    }
    else cout<< " ";
}


// } Driver Code Ends
/* The structure of the Linked list Node is as follows:

struct Node
{
    int data;
    Node *next;
    Node(int val)
    {
        data=val;
        next=NULL;
    }
};

*/

class Solution
{
    public:
    Node* findIntersection(Node* head1, Node* head2)
    {
        // code goes here.
        Node* temp1 = head1;
        Node* temp2 = head2;
        Node* newhead = nullptr;
        Node* newtemp = nullptr;
    
        while (temp1 != nullptr && temp2 != nullptr) {
            if (temp1->data > temp2->data) {
                temp2 = temp2->next;
            } else if (temp2->data > temp1->data) {
                temp1 = temp1->next;
            } else {
                if (newhead == nullptr) {
                    newhead = new Node(temp1->data);
                    newtemp = newhead;
                } else {
                    newtemp->next = new Node(temp1->data);
                    newtemp = newtemp->next;
                }
                temp1 = temp1->next;
                temp2 = temp2->next;
            }
        }
    
        return newhead; 
    }
};



//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n,m;
	    cin>> n >> m;
	    
	    Node* head1 = inputList(n);
	    Node* head2 = inputList(m);
	    
	    Solution ob;
	    Node* result = ob.findIntersection(head1, head2);
	    
	    printList(result);
	    cout<< endl;
	}
	return 0;
}

// } Driver Code Ends