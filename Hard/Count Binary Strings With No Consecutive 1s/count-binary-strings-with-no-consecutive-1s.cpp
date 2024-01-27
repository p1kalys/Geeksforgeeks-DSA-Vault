//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

typedef long long int ll;

class Solution {
  public:
    int mod = 1000000007;
    
    vector<vector<ll>> mul(vector<vector<ll>>& A, vector<vector<ll>>& B){
        int i, j;
        vector<vector<ll>> v(2, vector<ll>(2));
        
        v[0][0] = ((A[0][0]*B[0][0])%mod + (A[0][1]*B[1][0])%mod)%mod;
        v[0][1] = ((A[0][0]*B[0][1])%mod + (A[0][1]*B[1][1])%mod)%mod;
        v[1][0] = ((A[1][0]*B[0][0])%mod + (A[1][1]*B[1][0])%mod)%mod;
        v[1][1] = ((A[1][0]*B[0][1])%mod + (A[1][1]*B[1][1])%mod)%mod;
        
        return v;
        
    }
    
    vector<vector<ll>> bin_pow(vector<vector<ll>>& A, ll n){
        
        vector<vector<ll>> v(2, vector<ll>(2, 1));
        
        while(n > 0){
            if(n&1)
                v = mul(v, A);
            
            A = mul(A, A);
            n = n>>1;
        }
        
        return v;
    }
    
    int countStrings(long long int N) {
        // Code here
        
        vector<vector<ll>> v(2, vector<ll>(2));
        v[0][0] = 1;
        v[0][1] = 1;
        v[1][0] = 1;
        v[1][1] = 0;
        
        v = bin_pow(v, N);
        
        return v[0][0];
        
        
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        long long int N;
        cin >> N;
        Solution obj;
        cout << obj.countStrings(N) << endl;
    }
}
// } Driver Code Ends