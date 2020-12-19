#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

#define nodes 200001
int vis[nodes];
vector <int> temp;

void dfs(vector <int> graph[], int x)
{
    vis[x] = 1;
    temp.push_back(x);
    
    for(int u: graph[x])
        if(!vis[u])
            dfs(graph, u);
}



int main()
{
    ios_base::sync_with_stdio(0);
    int t, n, m, u, v;
    double mx;
    cin>>t;
    while(t--)
    {
        cin>>n>>m;
        vector <int> graph[n + 1];
        double a[n + 1], b[n + 1], used[n + 1];
        mx = 0;
        vector <int> ans;
        
        //initial steps
        temp.clear();
        for(int i = 1; i <= n; i++)
            cin>>a[i];
        for(int i = 1; i <= n; i ++)
            cin>>b[i];
        for(int i = 1; i <= n; i++)
            mx = max(mx, a[i] / b[i]);
        
        //making the new graph
        for(int i = 0; i < m; i++)
        {
            cin>>u>>v;
            if(a[u] / b[u] == mx && a[v] / b[v] == mx)
            {
                used[u] = 1;
                used[v] = 1;
                graph[u].push_back(v);
                graph[v].push_back(u);
            }
            else
            {
                if(a[u] / b[u] == mx)
                    used[u] = 1;
                if(a[v] / b[v] == mx)
                    used[v] = 1;
            }
        }
        
        //marking necessary nodes as visited and not visited
        for(int i = 1; i <= n; i++)
        {
            if(a[i] / b[i] == mx)
                vis[i] = 0;
            else
                vis[i] = 1;
        }
        
        
        //performing dfs on the nodes which have the max value
        for(int i = 1; i <= n; i++)
        {
            if(used[i] == 1 && vis[i] == 0)
            {
                temp.clear();
                dfs(graph, i);
                if(ans.size() < temp.size())
                    ans = temp;
            }
        }
        
        cout<<ans.size()<<endl;
        for(auto it: ans)
            cout<<it<<" ";
        cout<<endl;
        
    }
    return 0;
}
