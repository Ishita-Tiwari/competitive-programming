#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll n, k, p, parent[100005];
vector<pair<ll, ll> > a;

ll find(ll x)
{
	if(parent[x] == x) return x;
	return(find(parent[x]));
}


ll merge(ll a, ll b)
{
	if(find(a) < find(b))
		parent[find(b)] = find(a);
	else
		parent[find(a)] = find(b);
}


int main()
{
	cin>>n>>k>>p;
	for(ll i = 0; i < 100005; i ++)
		parent[i] = i;
	
	ll ele, l, r;
	
	for(ll i = 0; i < n; i++)
	{
		cin>>ele;
		a.push_back({ele, i});
	}
	
	sort(a.begin(), a.end());
	for(ll i = 1; i < n; i ++)
	{
		if ((a[i].first - a[i - 1].first) <= k)
			merge(a[i].second, a[i - 1].second);
	}
	
	for(ll i = 0; i < p; i++)
	{
		cin>>l>>r;
		if(find(l - 1) == find(r - 1))
			cout<<"Yes"<<"\n";
		else
			cout<<"No"<<"\n";
	}
}
