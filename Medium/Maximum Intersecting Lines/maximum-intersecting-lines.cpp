//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int maxIntersections(vector<vector<int>> l, int N) {
        // Code here
        vector<int>s,e;
        for(int i=0;i<l.size();i++) s.push_back(l[i][0]);
        for(int i=0;i<l.size();i++) e.push_back(l[i][1]);
        sort(s.begin(),s.end());
        sort(e.begin(),e.end());
        int i=1,j=0,c=1;
        while(i<l.size()){
            if(s[i++]<=e[j]) c++;
            else j++;
        }
        return c;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        vector<vector<int>> mat(N, vector<int>(2));
        for (int j = 0; j < 2; j++) {
            for (int i = 0; i < N; i++) {
                cin >> mat[i][j];
            }
        }
        Solution obj;
        cout << obj.maxIntersections(mat, N) << endl;
    }
}
// } Driver Code Ends