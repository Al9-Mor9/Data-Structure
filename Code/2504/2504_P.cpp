#include <iostream>
#include <stack>
using namespace std;

stack<int> stk;
int ans;
char str[31];

int main(){
    scanf("%s", str);
    for (int i = 0; str[i]; i++){
        if (str[i] == '('){
            stk.push(-'(');
        }
        else if (str[i] == '['){
            stk.push(-'[');
        }
        else if (str[i] == ')'){
            int tmp = 0;
            while (!stk.empty() && stk.top() > 0){
                tmp += stk.top();
                stk.pop();
            }
            if (stk.empty() || stk.top() == -'['){
                printf("0");
                return 0;
            }
            if (stk.top() == -'('){
                stk.pop();
                stk.push((tmp ? tmp : 1) * 2);
            }
        }
        else if (str[i] == ']'){
            int tmp = 0;
            while (!stk.empty() && stk.top() > 0){
                tmp += stk.top();
                stk.pop();
            }
            if (stk.empty() || stk.top() == -'('){
                printf("0");
                    return 0;
            }
            if (stk.top() == -'['){
                stk.pop();
                stk.push((tmp ? tmp : 1) * 3);
            }
        }
    }
    
    while (!stk.empty() && stk.top() > 0){
        ans += stk.top();
        stk.pop();
    }
    if (!stk.empty()) printf("0");
    else printf("%d", ans);

}


