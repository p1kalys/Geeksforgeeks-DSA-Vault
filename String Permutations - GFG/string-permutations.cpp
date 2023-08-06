//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
    public:
    //Complete this function
    void f(string S, int cur, vector<string> &res){
        if (cur==S.size()){
            res.push_back(S);
            return;
        }
        for(int i=cur; i<S.size();i++){
            swap(S[cur],S[i]);
            f(S,cur+1,res);
            swap(S[cur],S[i]);
        }
    }
    
    vector<string> permutation(string S)
    {
        //Your code here
        int cur=0;
        vector<string>res;
        f(S,cur,res);
        sort(res.begin(),res.end());
        return res;
    }
};

//{ Driver Code Starts.

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		string S;
		cin>>S;
		Solution ob;
		vector<string> vec = ob.permutation(S);
		for(string s : vec){
		    cout<<s<<" ";
		}
		cout<<endl;
	
	}
	return 0;
}
// } Driver Code Ends