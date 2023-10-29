//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
	int is_bleak(int n)
	{
	    int num=n-1;
	    int lim=32;
	    int count=0;
	    while(lim-- && count<n)
	    {
	        long long sum=num+ __builtin_popcount(num);
	        if(sum==n)
	        return false;
	        num--;
	        count++;
	    }
	    return true;
	}
};


//{ Driver Code Starts.
int main(){
    int T;
    cin >> T;
    while(T--)
    {
    	int n; 
    	cin >> n;
    	Solution ob;
    	int ans = ob.is_bleak(n);
    	cout << ans << "\n";
    }
	return 0;
}

// } Driver Code Ends