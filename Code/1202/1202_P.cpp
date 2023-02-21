#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int N, K, C[300000];
vector<pair<int, int>> jewel;
priority_queue<int> pq;

int main(){
    long long ans = 0;
    scanf("%d%d",&N, &K);
    jewel.resize(N);
    for (int i = 0; i <N; i++){
        scanf("%d%d", &jewel[i].first, &jewel[i].second);
    }

    for (int i = 0; i < K; i++){
        scanf("%d", &C[i]);
    }

    sort(jewel.begin(), jewel.end());
    sort(C, C + K);

    int idx = 0;
    for (int i = 0; i < K; i++){
        
        while (idx < N && C[i] >= jewel[idx].first){
            pq.push(jewel[idx].second);
            idx++;
        }

        if (!pq.empty()){
            ans += pq.top();
            pq.pop();
        }
    }
    printf("%lld", ans);
    
}
