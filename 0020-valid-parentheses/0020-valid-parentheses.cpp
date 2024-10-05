//Use Stack

// Rules 
// 1 push element if top element is not the closing bracket
// 2 pop the top element if the element to be pushed is the closing bracket
// after all the elements have been travesered we check if stack is empty if yes then Valid else Not Valid

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for(auto i : s) {
            if(stack.empty()) {
                stack.push(i);
            }
            else if((i == ')' && stack.top() == '(') || (i == '}' && stack.top() == '{') || (i == ']' && stack.top() == '[')) {
                stack.pop();
            }
            else {
                stack.push(i);
            }
        }

        return stack.empty();
    }
};