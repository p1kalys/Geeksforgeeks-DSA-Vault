//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class DisjointSet
{
    vector<int> parent,rank;
    public:
    DisjointSet(int n)
    {
        parent.resize(n+1);
        for(int i=0;i<=n;i++) parent[i]=i;
        rank.resize(n+1,0);
    }
    int findParent(int u)
    {
        if(parent[u]==u) return u;
        return parent[u]=findParent(parent[u]);
    }
    void Union(int u,int v)
    {
        u=findParent(u);
        v=findParent(v);
        if(rank[u]<rank[v])
        {
            parent[u]=v;
        }
        else if(rank[v]<rank[u])
        {
            parent[v]=u;
        }
        else
        {
            parent[v]=u;
            rank[u]++;
        }
    }
};


class Solution
{
    public:
    //Function to detect cycle using DSU in an undirected graph.
	int detectCycle(int V, vector<int>adj[])
	{
	    // Code here
	    DisjointSet DS(V);
    set<pair<int,int>> coveredEdge;
    for(int i=0;i<V;i++)
    {
        for(auto it:adj[i])
        {
            if(coveredEdge.find({i,it})!=coveredEdge.end() || coveredEdge.find({it,i})!=coveredEdge.end()) continue;
            if(DS.findParent(it)!=DS.findParent(i))
            {
                DS.Union(it,i);
                coveredEdge.insert({it,i});
            }
            else
            {
                return true;
            }
        }

    }
    return false;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int V, E;
		cin >> V >> E;
		vector<int>adj[V];
		for(int i = 0; i < E; i++){
			int u, v;
			cin >> u >> v;
			adj[u].push_back(v);
			adj[v].push_back(u);
		}
		Solution obj;
		int ans = obj.detectCycle(V, adj);
		cout << ans <<"\n";	}
	return 0;
}
// } Driver Code Ends