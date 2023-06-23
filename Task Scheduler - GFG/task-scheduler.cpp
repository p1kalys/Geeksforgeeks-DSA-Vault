//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int leastInterval(int N, int K, vector<char> &tasks) {
        // code here
        
        int maxFc=0;
        int counter[26]={0};
        int idle_count=0;
        int max_count=0;
        for(int i=0;i<N;i++)
        {
            counter[tasks[i]-'A']++;

        }
        for(auto x:counter){
            
            if (max_count==x){
                maxFc++;
            }
            if (max_count<x){
                maxFc=1;
                max_count=x;
            }
        }
        int gaps=max_count-1;
        int gap_len=K-(maxFc-1);
        int avail_slot=gaps*gap_len;
        int avail_task=N-max_count*maxFc;
    
        idle_count=max(0,avail_slot-avail_task);
      return N+idle_count;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, K;
        cin >> N >> K;

        vector<char> tasks(N);
        for (int i = 0; i < N; i++) cin >> tasks[i];

        Solution obj;
        cout << obj.leastInterval(N, K, tasks) << endl;
    }
    return 0;
}
// } Driver Code Ends