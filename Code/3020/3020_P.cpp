#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, H, h;
vector<int> up, down;
pair<int, int> ans;

int main(){
    scanf("%d%d", &N, &H);
    for (int i = 1; i <= N; i++){
        scanf("%d", &h);
        if (i % 2) {
            down.push_back(h);
        }
        else {
            up.push_back(h);
        }
    }
    sort(down.begin(), down.end());
    sort(up.begin(), up.end());

    ans = {N + 1, N + 1};
    for (int i = 1; i <= H; i++){
        int cnt_down = down.end() - lower_bound(down.begin(), down.end(), i);
        int cnt_up = up.end() - upper_bound(up.begin(), up.end(), H - i); 
        if (cnt_down + cnt_up < ans.first){
            ans = {cnt_down + cnt_up, 1};
        }
        else if (cnt_down + cnt_up == ans.first){
            ans.second++;
        }
    }

    printf("%d %d", ans.first, ans.second);
}
