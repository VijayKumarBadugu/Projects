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
    vector<int>v;
    int i;
    int k;
    for(i=0;i<N;i++)
    {
        cin>>k;
        v.push_back(k);
    }
    sort(v.begin(),v.end());
    
    for(i=0;i<N;i++)
    {
        cout<<v.at(i)<<" ";
    }
    
    return 0;
}
