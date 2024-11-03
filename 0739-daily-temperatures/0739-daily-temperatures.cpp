class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n,0);

        // Brute Force
        // int j;
        // for(int i = 0; i < n; i++) {
        //     for(j = i+1; j < n; j++) {
        //         if(temperatures[i] < temperatures[j]) {
        //             result[i] = j-i;
        //             break;
        //         }
        //     }
        // }

        // Using a Monotonic Stack i.e maintain a stack with inc or dec order
        stack<pair<int, int>> stack;

        for(int i = 0; i < n; i++) {
            int t = temperatures[i];
            while(!stack.empty() && t > stack.top().first) {
                auto pair = stack.top();
                stack.pop();
                result[pair.second] = i - pair.second;
            }
            stack.push({t, i});
        }

        return result;
    }
};