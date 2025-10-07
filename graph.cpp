#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;

    vector<vector<int>>arr(n+1);
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;

        arr[u].push_back(v);
    }
    for(int i=1;i<=n;i++){
        cout<<i ;
        for(int it:arr[i]){
            cout<<it;
        }
        cout<<"\n";
    }
    return 0;
}