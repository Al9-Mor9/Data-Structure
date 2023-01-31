#include <iostream>

using namespace std;

int N, node[27][2];


void preorder(int a) {
	if (!a) return;
	
	printf("%c", a + 64);
	preorder(node[a][0]);
	preorder(node[a][1]);

}

void inorder(int a) {
	if (!a) return;

	inorder(node[a][0]);
	printf("%c", a + 64);
	inorder(node[a][1]);

}

void postorder(int a) {
	if (!a) return;

	postorder(node[a][0]);
	postorder(node[a][1]);
	printf("%c", a + 64);

}


int main() {
	char root, left, right;
	scanf("%d", &N);
	while (N--) {
		scanf("%*[\n] %c %c %c", &root, &left, &right);

		node[root - 64][0] = left == '.' ? 0 : left - 64;
		node[root - 64][1] = right == '.' ? 0 : right - 64;
	}

	preorder(1);
	printf("\n");
	inorder(1);
	printf("\n");
	postorder(1);

}
