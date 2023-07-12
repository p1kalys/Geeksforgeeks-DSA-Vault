//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;
vector<string> AllParenthesis(int n) ;


// } Driver Code Ends
//User function Template for C++

// N is the number of pairs of parentheses
// Return list of all combinations of balanced parantheses
class Solution
{
    vector<string>res;
    public:
    vector<string> AllParenthesis(int n) 
    {
        // Your code goes here 
    
        string s="";
        generate(s,n,n);
        return res;
    }
    void generate(string s,int o,int c){
        if (o==0 && c==0){
            res.push_back(s);
            return;
        }
        if (o>0){
            s.push_back('(');
            generate(s,o-1,c);
            s.pop_back();
        }
        if (c>0){
            if (o<c){
                s.push_back(')');
                generate(s,o,c-1);
                s.pop_back();
            }
        }
    }
};

//{ Driver Code Starts.


int main() 
{ 
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		Solution ob;
		vector<string> result = ob.AllParenthesis(n); 
		sort(result.begin(),result.end());
		for (int i = 0; i < result.size(); ++i)
			cout<<result[i]<<"\n";
	}
	return 0; 
} 

// } Driver Code Ends