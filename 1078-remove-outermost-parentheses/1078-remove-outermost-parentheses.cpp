// Soln 1 :- Lets make Rules eg ( -> ) or ) -> ( , this will lead to many rules
// Soln 2 :- Using depth keep track of the depth.

class Solution {
public:
    string removeOuterParentheses(string s) {
        string result;
        int depth = 0;
        for(const auto& i :s){
            if(i == '('){
                if(depth > 0){
                    result.push_back(i);
                }
                depth++;
            }
            else{
                depth--;
                if(depth > 0){
                    result.push_back(i);
                }
            }
        }
        return result;
    }
};