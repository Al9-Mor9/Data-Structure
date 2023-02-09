#include <iostream>
#include <unordered_map>
#include <string>
#include <set>
using namespace std;

class Node{
    public : 
        int depth = 0;
        unordered_map<char, Node*> child;
        Node(){}
        Node(int d) {
            depth = d;
        }

        void insert(string word, int idx){
            if (!word[idx]){
                child['*'] = new Node(depth + 1);
                return;
            }
            if (child.count(word[idx])) {
                child[word[idx]]->insert(word, idx + 1);            
            }
            else {
                child[word[idx]] = new Node(depth + 1);
                child[word[idx]]->insert(word, idx + 1);
            }
        }

        bool find(string word, int idx){
            if (child.count(word[idx])){
                return child[word[idx]]->find(word, idx + 1);
            }
            if (depth == word.length() && child.count('*')) return true;
            return false; 
        }

};

void dfs(Node* node, int length, int x, int y, string board[4], string result);
Node head = Node();
int w, b;
string word, longestWord, result;
set<string> found;
string board[4];
bool visited[4][4];
int dir[8][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}, {1, -1}, {-1, 1}, {1, 1}, {-1, -1}};
int score;

int main(){
    cin >> w;
    for (int i = 0; i < w; i++){
        cin >> word;
        head.insert(word , 0);
    }
    cin >> b;
    for (int i = 0; i < b; i++){
        found.clear();
        result = "";
        longestWord = "";
        score = 0;
        for (int i = 0; i < 4; i++) cin >> board[i];
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 5; j++){
                if (!head.child.count(board[i][j])) continue;
                visited[i][j] = true;
                dfs(head.child[board[i][j]], 1, i, j, board, result);
                visited[i][j] = false;
            }
        }
        cout << score << " " << longestWord << " " << found.size() << endl;
    } 
}


void dfs(Node* node, int length, int x, int y, string board[4], string result){
    if (length > 8) return;
    string cpy = result + board[x][y];
    if (head.find(cpy, 0)) {   
        if (longestWord.length() < cpy.length()) longestWord = cpy;
        else if (longestWord.length() == cpy.length() && longestWord > cpy) longestWord = cpy;
        if (found.count(cpy) == 0){
            found.insert(cpy);
            switch (cpy.length()){
                case 3:
                case 4: score += 1; break;
                case 5: score += 2; break;
                case 6: score += 3; break;
                case 7: score += 5; break;
                case 8: score += 11; break;
                default : break;
            }
        }
    }
    for (int i = 0; i < 8; i++){
        int nextX = x + dir[i][0]; 
        int nextY = y + dir[i][1];
        if (nextX < 0 || nextY < 0 || nextX >=4 || nextY >= 4) continue;
        if (visited[nextX][nextY]) continue;
        char c = board[nextX][nextY];
        if (!(node->child.count(c))) continue;
        visited[nextX][nextY] = true;
        dfs(node->child[c], length + 1, nextX, nextY, board, cpy);
        visited[nextX][nextY] = false;
    }    
}
