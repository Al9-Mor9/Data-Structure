#include <iostream>
#include <algorithm>
using namespace std;
#define NMAX 50000

int n, y, r, m, Y, X;
int year[NMAX];
int rain[NMAX];
int tree[NMAX * 4];

int max(int a, int b){
	return a > b ? a : b;
}

int makeTree(int start, int end, int root){
	if (start == end) {
		tree[root] = rain[start];
		return tree[root];
	}
	int mid = (start + end) / 2;
	tree[root] = max(makeTree(start, mid, root * 2), makeTree(mid + 1, end, root * 2 + 1));
	return tree[root];
}

int segSearch(int start, int end, int root, int left, int right){
	if (right < start || end < left) return 1;
	//printf("[%d] (%d ~ %d) -> %d : (%d ~ %d)\n", root, start, end, tree[root], left, right);
	if (left <= start && end <= right) return tree[root];
	int mid = (start + end) / 2;
	return max(segSearch(start, mid, root * 2, left, right), segSearch(mid + 1, end, root * 2 + 1, left, right));
}

int main(){
	scanf("%d", &n);
	for (int i = 0; i < n; i++){
		scanf("%d%d", &y, &r);
		year[i] = y;
		rain[i] = r;
	}
	makeTree(0, n, 1);

	scanf("%d", &m);
	for (int i = 1; i < m; i++){
		scanf("%d%d", &Y, &X);
		bool yExists = false;
		bool xExists = false;
		bool xSmaller = false;

		int xLBIdx = lower_bound(year, year + n, X) - year;
		int yLBIdx = lower_bound(year, year + n, Y) - year;

		if (year[yLBIdx] == Y) yExists = true;
		if (year[xLBIdx] == X) xExists = true;
		
		if (yExists && xExists){
			if (rain[xLBIdx] <= rain[yLBIdx]) {
				int maxRain = segSearch(0, n, 1, yLBIdx + 1, xLBIdx- 1);
				if (X - Y == 1) printf("true\n");
				else if (maxRain < rain[xLBIdx]) {
					if (year[xLBIdx] - year[yLBIdx] == xLBIdx - yLBIdx) printf("true\n");
					else printf("maybe\n");
				}
				else printf("false\n");
			}
			else printf("false\n");
		}
		else if (yExists){//y는 확실한데 x는 아닌 경우 : y의 다음 해 ~ x보다 작은 가장 큰 연도를 고려해야 함
			if (X - Y == 1) printf("maybe\n");
			else {
				int maxRain = segSearch(0, n, 1, yLBIdx + 1, xLBIdx - 1);
				if (rain[yLBIdx] > maxRain) printf("maybe\n");
				else printf("false\n");
			}
		}
		else if (xExists){//x는 있는데 y는 아닌 경우
			if (X - Y == 1) printf("maybe\n");
			else {
				int maxRain = segSearch(0, n, 1, yLBIdx, xLBIdx - 1);
				if (rain[xLBIdx] > maxRain) printf("maybe\n");
				else printf("false\n");
			}
		}
		else {//둘 다 모르는 경우
			int maxRain = segSearch(0, n, 1, yLBIdx, xLBIdx - 1);
			if (maxRain == 1000000000) printf("false\n");
			else printf("maybe\n");
		}
	}
}
