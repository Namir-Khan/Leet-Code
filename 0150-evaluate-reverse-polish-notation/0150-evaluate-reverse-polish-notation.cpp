// Use Stack
// push tokens in stack until an operation is found
// when found pop the last 2 elements and do the operation and push the result back in the stack

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        int a,b;
        for(auto & i : tokens) {
            if(i == "+") {
                b = s.top();
                s.pop();
                a = s.top();
                s.pop();
                s.push(a+b);
            }
            else if(i == "-") {
                b = s.top();
                s.pop();
                a = s.top();
                s.pop();
                s.push(a-b);
            }
            else if(i == "/") {
                b = s.top();
                s.pop();
                a = s.top();
                s.pop();
                s.push(a/b);
            }
            else if(i == "*") {
                b = s.top();
                s.pop();
                a = s.top();
                s.pop();
                s.push(a*b);
            }
            else {
                s.push(stoi(i));
            }
        }
        return s.top();
    }
};