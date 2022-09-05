#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
signed main(){
    ll h,w;
    cin>>h>>w;
    ll ara[h][w],bra[w][h];
    for(ll i=0;i<h;i++){
        for(ll j=0;j<w;j++){
            cin>>ara[i][j];
        }
    }
    for(ll i=0;i<w;i++){
        for(ll j=0;j<h;j++){
            bra[i][j]=ara[j][i];
        }
    }
    for(ll i=0;i<w;i++){
        for(ll j=0;j<h;j++){
            cout<<bra[i][j];
            if(j<h)cout<<" ";
            else cout<<endl;
        }
    }
    return 0;
}