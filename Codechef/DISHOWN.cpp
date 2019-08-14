#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll parent[100005], s[100005], t, n, q, num, x, y, px, py;

int find(ll x)
{
    if(x == parent[x])
        return(x);
    else
        return(parent[x] = find(parent[x]));
}

int main() {
	cin>>t;
	while(t--)
	{
	    cin>>n;
	    for(ll i = 1; i <= n; i++)
	    {
	        cin>>s[i];
	        parent[i] = i;
	    }
	   cin>>q;
	   while(q--)
	   {
	       cin>>num;
	       if(num == 0)
	       {
	           cin>>x>>y;
	           px = find(x);
	           py = find(y);
	           if(px == py)
	                cout<<"Invalid query!"<<"\n";
	           else
	           {
	                if(s[px] > s[py])
	                    parent[py] = px;
	                if(s[px] < s[py])
	                    parent[px] = py;
	           }
	       }
	       else
	       {
	           cin>>x;
	           cout<<find(x)<<"\n";
	       }
	   }
	}
	return 0;
}

