//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
public:
    void rotate(vector<vector<int> >& matrix) {
        // Code here
        int n= matrix.size();
        int m=matrix[0].size();
        for(int i=0; i<n/2; i++){
            for(int j=0; j<m; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n-1-i][m-1-j];
                matrix[n-1-i][m-1-j] = temp;
            }
        }
        if(n%2!=0){
            for(int i=0; i<m/2; i++){
                swap(matrix[n/2][i], matrix[n/2][m-i-1]);
            }
        }
    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<vector<int>> matrix(n, vector<int>(n,0));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cin >> matrix[i][j];
			}
		}
		Solution ob;
		ob.rotate(matrix);
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++)
				cout << matrix[i][j] <<" ";
			cout << "\n";
		}
	}
	return 0;
}
// } Driver Code Ends