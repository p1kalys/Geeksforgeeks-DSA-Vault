//{ Driver Code Starts
// C++ program to check if two strings are isomorphic


#include<bits/stdc++.h>


using namespace std;
#define MAX_CHARS 256

// } Driver Code Ends
class Solution
{
    public:
    //Function to check if two strings are isomorphic.
    bool areIsomorphic(string str1, string str2)
    {
        int n = str1.size(), m = str2.size();
        unordered_map<char, char> mp;
        if (n != m) return false;
        for (int i = 0; i < n; i++) {
            if (mp.find(str1[i]) != mp.end()) {
                if (mp[str1[i]] != str2[i]) {
                    return false;
                }
            } else {
                // Check if the character in str2 is already mapped to some other character in str1
                for (auto it = mp.begin(); it != mp.end(); ++it) {
                    if (it->second == str2[i]) {
                        return false;
                    }
                }
                mp[str1[i]] = str2[i];
            }
        }
        return true;
    }
};

//{ Driver Code Starts.

// Driver program
int main()
{
    int t;
    cin>>t;
    string s1,s2;
    while (t--) {
        cin>>s1;
        cin>>s2;
        Solution obj;
        cout<<obj.areIsomorphic(s1,s2)<<endl;
    }
    
    return 0;
}
// } Driver Code Ends