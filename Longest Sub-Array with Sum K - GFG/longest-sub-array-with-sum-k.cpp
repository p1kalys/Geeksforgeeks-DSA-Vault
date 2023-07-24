//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
    public:
    int lenOfLongSubarr(int nums[],  int n, int k) 
    { 
        // Complete the function
        int ans=0;
        int sum=0;
        
        unordered_map<int,int>mp;
        for(int i=0; i<n;i++){
            sum+=nums[i];
            if(sum==k){
                ans=max(ans,i+1); 
            }
            if (mp.find(sum)==mp.end()) {
                mp[sum]=i;
            }
            if (mp.find(sum-k)!=mp.end()){
                ans=max(ans,i-mp[sum-k]);
            }
        }
        return ans;

    } 

};

//{ Driver Code Starts.

int main() {
	//code
	
	int t;cin>>t;
	while(t--)
	{
	    int n, k;
	    cin>> n >> k;
	    int a[n];
	    
	    for(int i=0;i<n;i++)
	        cin>>a[i];
	   Solution ob;
	   cout << ob.lenOfLongSubarr(a, n , k)<< endl;
	    
	}
	
	return 0;
}
// } Driver Code Ends