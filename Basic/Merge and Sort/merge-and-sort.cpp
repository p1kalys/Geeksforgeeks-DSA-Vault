//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
    // Write your code here

class Solution{
    public:
    int mergeNsort(int a[], int b[], int N, int M, int answer[])
    {
        // Write your code here
        int i1=0,i2=0;
        int i=0;
        while(i1<N && i2<M){
            if(a[i1]==b[i2]){
                 answer[i]=a[i1];
                 i1++;
                 i++;
                 i2++;
            }
            else if(a[i1]<b[i2]){
                answer[i]=a[i1];
                i1++;
                i++;
            }
            else {
                answer[i]=b[i2];
                i2++;
                i++;
            }
        }
        while(i1<N){
            answer[i]=a[i1];
            i1++;                
            i++;
        }
        while(i2<M){
            answer[i]=b[i2];
            i2++;
            i++;
        }
        
        sort(answer, answer+i);
        int newSize = unique(answer, answer + i) - answer;
        return newSize;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n, m;
        cin>>n;
        int a[n+5];
        for(int i=0;i<n;i++)
            cin>>a[i];
        cin>>m;
        int b[m+5];
        for(int j=0;j<m;j++)
            cin>>b[j];
        Solution ob;
        int answer[n+m+5];
        int x=ob.mergeNsort(a, b, n, m, answer);
        
        for(int i=0;i<x;i++)
        cout<<answer[i]<<" ";
        cout<<endl;
    }
	
	return 0;
}
// } Driver Code Ends