class Solution {
public:

    void backtrack (int openN, int closeN, int n, string& stack, vector<string>& result) {
        if(openN == n && closeN == n) {
            result.push_back(stack);
            return;
        }

        if(openN < n) {
            stack += '(';
            backtrack(openN + 1, closeN, n, stack, result);
            stack.pop_back();
        }

        if(closeN < openN) {
            stack += ')';
            backtrack(openN, closeN + 1, n, stack, result);
            stack.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string stack;
        backtrack(0, 0, n, stack, result);
        return result;
    }
};