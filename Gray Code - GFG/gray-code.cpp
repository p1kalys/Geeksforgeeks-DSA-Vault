//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution
{
    public:
    vector<string> graycode(int n)
    {
        vector<string>graystring = generate(n);
        return graystring;    
    }
    vector<string> generate(int n){
        if (n==1){
            return {"0","1"};
        }
        vector<string>ans;
        vector<string>temp = generate(n-1);
        for(int i=0; i<temp.size(); i++){
            ans.push_back("0"+temp[i]);
        }
        for(int i=temp.size()-1; i>=0; i--){
            ans.push_back("1"+temp[i]);
        }
        return ans;
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
        vector<string> ans= ob.graycode(n);
        for(int i=0;i<ans.size();i++)
            cout<<ans[i]<<" ";
            
        cout<<"\n";
    }
}




// } Driver Code Ends