#include<iostream>
#include <map>
#include <string>
using namespace std;

map<string, int> m;
int cnt;

int main(){
    string tree;
    while (!cin.eof()){
        getline(cin, tree);
        if (tree == "") continue;
        m[tree] += 1;
        cnt += 1;
    }
    for (pair<string, int> p : m){
        cout << p.first;
        printf(" %.4lf\n", (double) p.second * 100 / cnt);
    }


}
