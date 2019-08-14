#include<bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b)
{
	if(a == 0)
		return(b);
	return(gcd(b % a, a));
}

int main()
{
	long long t;
	cin>>t;
	while(t--)
	{
		long long n, g1, g2, ans, ans1, ans2, case1, case2, case3, case4, val, ele, gfir, gsec, ind, ind2, num = 0;
		cin>>n;
		long long a[n];
		long long l1[n], l2[n];
		for(int i = 0; i < n; i++)
			cin>>a[i];
		sort(a, a+n);
		if(a[0] == a[n - 1])
		    cout<<(2 * a[0])<<"\n";
		else
		{
    		for(long long i = 0; i < n ; i++)
    		{
    			if (a[i] == a[n - 1])
    			{
    				ind = i;
    				break;
    			}
    		}
    		for(long long i = ind, j = 0; i < n; i ++, j++)
    			l1[j] = a[i];
    		l2[0] = a[ind - 1];
    		g1 = l1[0];
    		g2 = l2[0];
    		
    		for(long long i = 0; i < ind - 1; i ++)
    		{
    			ele = a[i];
    			gfir = gcd(ele, g1);
    			gsec = gcd(ele, g2);
    			ans1 = gfir + g2;
    			ans2 = gsec + g1;
    			
    			if (ans1 > ans2)
    			    g1 = gfir;
    			else
    			    g2 = gsec;
    		}
    		case1 = g1 + g2;
    		
    		g1 = l1[0];
    		g2 = l2[0];
    		for(long long i = ind - 2; i >= 0; i--)
    		{
    			ele = a[i];
    			gfir = gcd(ele, g1);
    			gsec = gcd(ele, g2);
    			if (gfir > gsec)
    			    g1 = gfir;
    			else
    			    g2 = gsec;
    		}
    		case2 = g1 + g2;
    		
    		
    		if(ind > 0)
    		{
    			val = a[ind - 1];
    			for(long long i = n - 2; i >= 0; i--)
    			{
    				if(a[i] != a[n - 1])
    					val = gcd(val, a[i]);
    			}
    			case3 = val + a[n - 1];
    		}
    		else
    			case3 = a[0] * 2;
    		for(long long i = 0; i < n; i++)
    			l1[i] = 0;
    		ind2 = ind - 1;
    		for(long long i = 0, j = 0; i < n; i++)
    		{
    			if(a[i] != a[ind2])
    			{
    				l1[j] = a[i];
    				j++;
			}
			num = j;
		}
    		gfir = l1[0];
    		for(long long i = 0; i < num; i++)
    		{
    			ele = l1[i];
    			gfir = gcd(ele, gfir);
			}
		case4 = gfir + a[ind2];

    		ans1 = max(case1, case2);
    		ans2 = max(case3, case4);
    		ans = max(ans1, ans2);
    		cout<<ans<<"\n";
		}
	}
}
