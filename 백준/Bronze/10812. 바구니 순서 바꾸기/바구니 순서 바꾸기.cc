#include <iostream>
using namespace std;

int main()
{
    int n, m, begin, mid, end, t;
    int arr[101]={0,};
    int temp[101]={0,};
    cin >> n >> m;
    
    
    for(int i=1;i<=n;i++){
        arr[i]=i;

    }

    for(int i=0;i<m;i++){
        cin >> begin >> end >> mid;
        t=0;
        
        for(int j=begin;j<mid;j++){
            temp[j]=arr[j];
        }
        
        for(int j=mid;j<=end;j++){
            arr[begin+t]=arr[j];
            t++;
        }//mid부터 end까지
        
        for(int j=begin;j<mid;j++){
            arr[begin+t]=temp[j];
            t++;
        }
    }
    for(int j=1;j<=n;j++){
        cout << arr[j] <<" ";
    }
}
