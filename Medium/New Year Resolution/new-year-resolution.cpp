//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution {
    int helper(int ind,int arr[],int sum,vector<vector<int>>&dp){
        if((sum%20==0 or sum%24==0)and sum!=0)return 1;
        if(ind==0){
            if((sum+arr[0])%20==0 or
                (sum+arr[0])%24==0 or
                (sum+arr[0]==2024))return 1;
            else return 0;
        }
        if(dp[ind][sum]!=-1)return dp[ind][sum];
        return dp[ind][sum]= (helper(ind-1,arr,sum+arr[ind],dp) or helper(ind-1,arr,sum,dp));
    }
    
    public:
    int isPossible(int N , int coins[]) 
    {
        
        vector<vector<int>>dp(N,vector<int>(2025,-1));
        //memeset(dp,sizeof(dp),-1);
        return helper(N-1,coins,0,dp);
        
    }
    
};




//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        
        cin>>N;
        int coins[N];
        for(int i=0 ; i<N ; i++)
            cin>>coins[i];

        Solution ob;
        cout << ob.isPossible(N,coins) << endl;
    }
    return 0;
}
// } Driver Code Ends