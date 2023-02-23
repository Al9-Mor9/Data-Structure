#include <iostream>
using namespace std;
#define CANDYMAX 1000001

int n, a, b, c;
int tree[CANDYMAX * 4];

int getCandy(int start, int end, int root, int val){
    if (end < start) return 0;
    if (tree[root] < val) return 0;
    if (start == end) return start;
    int mid = (start + end) / 2;
    if (tree[root * 2] >= val) return getCandy(start, mid, root * 2, val);
    return getCandy(mid + 1, end, root * 2 + 1, val - tree[root * 2]);
}

void update(int start, int end, int root, int index, int amt){
    if (index < start || end < index) return;
    tree[root] += amt;
    if (start == end) return;
    int mid = (start + end) / 2;
    update(start,   mid, root * 2,     index, amt);
    update(mid + 1, end, root * 2 + 1, index, amt);
}

int main(){
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        scanf("%d", &a);
        if (a == 1){
            scanf("%d", &b);
            int candy = getCandy(0, CANDYMAX, 1, b);
            update(0, CANDYMAX, 1, candy, -1);
            printf("%d\n", candy);
        }
        else {
            scanf("%d%d", &b, &c);
            update(0, CANDYMAX, 1, b, c);
        }
    }
}
