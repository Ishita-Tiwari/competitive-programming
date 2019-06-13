#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	
	while(t--)
	{
		string n;
		cin>>n;
		long long ans = 0;
		for(int i = 0; i < n.size(); i++)
		{
			if(n[i] != '4' && n[i] != '7')
				ans++;
		}
		cout<<ans<<"\n";
	}
}
