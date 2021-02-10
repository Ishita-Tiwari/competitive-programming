#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll calc(ll l[], ll n)
{
    ll count = 0;
    for(ll i = 0; i < n; i++)
    {
        if(l[i] - 1 != i)
        {
            count++;
            break;
        }
    }
    return(count);
}

ll gcd(ll a, ll b)
{
    if(a == 0)
        return(b);
    return(gcd(b % a, a));
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    
    ll t;
    cin>>t;
    ll n, k, a, va, b, vb, c, vc, d, vd;
    while(t--)
    {
        cin>>n>>k;
        ll l[n];
        bool flag = true;
        unordered_map<ll, ll>mp;
        set<pair<ll,ll>> st;
        vector<vector<ll>>ans;
        
        for(ll i = 0; i < n; i++)
           {
            cin>>l[i];
            if(l[i] - 1 != i)
                mp[i] = l[i];
        }
        
        ll chk = gcd(n, k);
        
        while(!mp.empty())
        {
            a = mp.begin() -> first;
            va = l[a];
            b = va - 1;
            vb = l[b];
            c = vb - 1;
            
            if(vb == a + 1)
            {
                mp.erase(a);
                mp.erase(b);
                continue;
            }
            vc = l[c];
            if(a == b || b == c || c == a || flag == false)
            {
                flag = false;
                break;
            }
            mp[a] = vc; mp[b] = va; mp[c] = vb;
            l[b] = va; l[c] = vb; l[a] = vc;
            
            vector<ll> temp;
            temp.push_back(a + 1);
            temp.push_back(b + 1);
            temp.push_back(c + 1);
            ans.push_back(temp);
            
            if(l[a] == a + 1)
                mp.erase(a);
            if(l[b] == b + 1)
                mp.erase(b);
            if(mp[c] == c + 1)
                mp.erase(c);
        }
        
        for(ll i = 0; i < n; i++)
        {
            a = i;
            va = l[a];
            if(l[i] == i + 1)
                continue;
            b = va - 1;
            vb = l[b];
            
            if(vb == a + 1)
            {
                ll mn;
                mn = min(a, b);
                st.insert({mn, (a + b) - mn});
            }
        }
        
        
        auto fr = st.begin();
        if(st.size() % 2 != 0)
            ++fr;
        
        for(; fr != st.end(); )
        {
            a = fr -> first;
            va = l[a];
            b = fr -> second;
            vb = l[b];
            ++fr;
            c = fr -> first;
            vc = l[c];
            d = fr -> second;
            vd = l[d];
            
            l[c] = vd;
            l[d] = vc;
            l[a] = vb;
            l[b] = va;
            
            vector<ll> tmp1, tmp2;
            tmp1.push_back(a + 1);
            tmp1.push_back(b + 1);
            tmp1.push_back(c + 1);
            tmp2.push_back(c + 1);
            tmp2.push_back(a + 1);
            tmp2.push_back(d + 1);
            ans.push_back(tmp1);
            ans.push_back(tmp2);
            
            ++fr;
        }
        
        //ll now;
        //now = calc(l, n);
        ll count = 0;
        for(ll i = 0; i < n; i++)
        {
            if(l[i] - 1 != i)
            {
                flag = false;
                break;
            }
        }
        if(ans.size() > k || flag == false)
            cout<<"-1"<<"\n";
        else
        {
            cout<<ans.size()<<"\n";
            for(auto i: ans)
                cout<<i[0]<<" "<<i[1]<<" "<<i[2]<<"\n";
        }
    }
    return 0;
}
