//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// #define ll long long
#define ll long long
#define mod 1000000007
class Solution{
public:
    vector<long long> nthRowOfPascalTriangle(int n) 
    {
       vector<vector<ll>>v1(n,vector<ll>(n,0));
       
       if(n==1) return {1};
       
       v1[0][0]=1;
       
       for(int i=1;i<n;i++)
       {
           for(int j=0;j<=i;j++)
           {
               if(j==0)
               {
                 v1[i][j]=v1[i-1][j];
               }
               else
               {
                   v1[i][j]=(v1[i-1][j-1]%mod+v1[i-1][j]%mod)%mod;
               }
           }
       }
       return v1[n-1];
       
    }
};


//{ Driver Code Starts.


void printAns(vector<long long> &ans) {
    for (auto &x : ans) {
        cout << x << " ";
    }
    cout << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution ob;
        auto ans = ob.nthRowOfPascalTriangle(n);
        printAns(ans);
    }
    return 0;
}

// } Driver Code Ends