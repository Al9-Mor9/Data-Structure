#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int K, N, pr, cnt;
priority_queue<int, vector<int>, greater<>> pq;
vector<int> primeVector;

int main(){
    scanf("%d%d", &K, &N);
    for (int i = 0; i < K; i++) {
        scanf("%d", &pr);
        primeVector.push_back(pr);
    }
    pq.push(1);
    while (cnt != N){
        int top = pq.top();
        while(!pq.empty() && pq.top() == top) {
            pq.pop();
        }
        cnt++;
        for (int p : primeVector) if ((long long) p * top < (1LL << 31)) pq.push(p * top);
    }
    printf("%d", pq.top());
}
