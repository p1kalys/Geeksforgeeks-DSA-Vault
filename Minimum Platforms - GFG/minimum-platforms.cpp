//{ Driver Code Starts
// Program to find minimum number of platforms
// required on a railway station
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
    public:
    //Function to find the minimum number of platforms required at the
    //railway station such that no train waits.
    static bool cmp(pair<int,char> a, pair<int,char> b){
         if(a.first == b.first) return a.second < b.second;
        return a.first < b.first;
    }
    int findPlatform(int av[], int dp[], int n)
    {
    	vector<pair<int,char>>a;
    	for(int i=0;i<n;i++){
    	    a.push_back({av[i],'a'});
    	    a.push_back({dp[i],'d'});
    	}
    	sort(a.begin(),a.end(),cmp);
    	int res=1;
    	int c=0;
    	for(auto it:a){
    	    if(it.second=='a')
    	        c++;
    	    else
    	        c--;
    	   res=max(c,res);
    	}
    	return res;
    }
};


//{ Driver Code Starts.
// Driver code
int main()
{
    int t;
    cin>>t;
    while(t--) 
    {
        int n;
        cin>>n;
        int arr[n];
        int dep[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        for(int j=0;j<n;j++){
            cin>>dep[j];
        }
        Solution ob;
        cout <<ob.findPlatform(arr, dep, n)<<endl;
    } 
   return 0;
}
// } Driver Code Ends