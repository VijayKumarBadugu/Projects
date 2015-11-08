#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int N;
    cin>>N;
    int i;
    
    vector<int>v;
    int k;
    for(i=0;i<N;i++)
    {
        cin>>k;
        v.push_back(k);
    }
    
    cin>>k;
    v.erase(v.begin()+k-1);
    cin>>k;
    int j;
    cin>>j;
    v.erase(v.begin()+k-1,v.begin()+j-1);
    cout<<v.size()<<"\n";
    for(i=0;i<v.size();i++)
    {
        cout<<v.at(i)<<" ";
    }
    
    return 0;
}
