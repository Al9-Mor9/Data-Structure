#include <iostream>
#include <stack>
using namespace std;

stack<int> stk;
int ans;
char str[31];

int main(){
    scanf("%s", str);                               //괄호 문자열을 입력 받습니다
    for (int i = 0; str[i]; i++){                   //해당 문자열을 처음부터 읽어 갑니다. 문자열의 경우 마지막이 0이므로 따로 문자열의 길이를 구할 필요 없이 문자가 0이 되기 전까지 읽어가면 됩니다.
        if (str[i] == '('){                         //여는 괄호를 만난다면 해당 값에 -1을 곱해 스택에 쌓아줍니다.
            stk.push(-'(');                         //굳이 -1을 곱할 필요는 없고, '('와 '['에 서로 중복되지 않는 음수 값을 부여해줘도 됩니다.
        }
        else if (str[i] == '['){
            stk.push(-'[');
        }
        else if (str[i] == ')'){                
            int tmp = 0;
            while (!stk.empty() && stk.top() > 0){  //닫는 괄호를 만났다면 스택에서 0보다 큰 수들을 차례대로 뽑아 더해줍니다. (tmp)
                tmp += stk.top();
                stk.pop();
            }
            if (stk.empty() || stk.top() == -'['){  //양수를 다 뽑았을 때, 스택이 비어있거나 스택의 top과 닫는 괄호가 짝이 맞지 않는 경우입니다. 바로 0을 출력하고 종료합니다.
                printf("0");
                return 0;
            }
            if (stk.top() == -'('){                 //닫는 괄호의 짝을 찾았다면 pop하고, tmp에 값을 곱해 다시 push해줍니다.
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
    
    while (!stk.empty() && stk.top() > 0){          //만약 위 작업이 성공적으로 끝났다면 스택에는 양의 정수들만 남아 있게 됩니다. 스택에 남은 모든 수를 더해주면 답이 됩니다.
        ans += stk.top();
        stk.pop();
    }
    if (!stk.empty()) printf("0");                  //하지만 만약 여전히 스택에 남은 게 있다면 여는 괄호에 해당하는 값(음수)가 남아있다는 것이므로 0을 출력해줍니다. 그렇지 않으면 답을 출력합니다.
    else printf("%d", ans);

}


