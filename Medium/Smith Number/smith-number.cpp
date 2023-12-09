//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
  public:
    int smithNum(int n) {
        // code here
        int prime=0;
        int digit=0;
        int num=n;
        int flag=0;
        int num2=n;
        for(int i=2; i<num2; i++){
            if(num2%i==0){
                flag=1;
                break;
            }
        }
        if(flag==0){
            return 0;
        }
        while(num>0){
            int rem=num%10;
            digit=digit+rem;
            num=num/10;
        }
        while(n%2==0){
            prime=prime+2;
            n=n/2;
        }
        for(int i=3; i*i<=n; i+=2){
            while(n%i==0){
                int res=i;
                while(res){
                    prime+=res%10;
                    res/=10;
                }
                //prime+=i;
                n=n/i;
            }
        }
        if(n>2){
            while(n>0){
                prime=prime+n%10;
                n=n/10;
            }
        }
        if(prime==digit){
            return 1;
        }
        else{
            return 0;
        }
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        
        cin>>n;

        Solution ob;
        cout << ob.smithNum(n) << endl;
    }
    return 0;
}
// } Driver Code Ends