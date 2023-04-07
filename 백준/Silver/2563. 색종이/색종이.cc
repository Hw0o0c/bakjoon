#include <iostream>
using namespace std;

int main()
{
    int x,y,T,ans=0;
    int xy[101][101]={0,};
    cin >> T;

    for(int i=0; i < T; i++){
        cin >> x >> y;
        for(int j=x;j<x+10;j++){
            for(int k=y;k<y+10;k++){
                xy[j][k]+=1;
                if(xy[j][k]==1){ans++;}
            }
        }
    }
    cout << ans;
}
