//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int maxGold(int n, int m, vector<vector<int>> M)
    {
        // code here
        int  dp[n+2][m+1];
        for(int i=0;i<n+2;i++){
            for(int j=0;j<m+1;j++)
                dp[i][j]=0;
        }
        
        for(int j=0;j<m;j++){
            for(int i=0;i<n;i++){
                dp[i+1][j+1] = max({dp[i][j],dp[i+1][j],dp[i+2][j]})+M[i][j];
            }
        }
        int ans = -1;
        for(int i=0;i<n+2;i++){
            ans = max(ans,dp[i][m]);
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n, m;
        cin>>n>>m;
        vector<vector<int>> M(n, vector<int>(m, 0));
        for(int i = 0;i < n;i++){
            for(int j = 0;j < m;j++)
                cin>>M[i][j];
        }
        
        Solution ob;
        cout<<ob.maxGold(n, m, M)<<"\n";
    }
    return 0;
}
// } Driver Code Ends