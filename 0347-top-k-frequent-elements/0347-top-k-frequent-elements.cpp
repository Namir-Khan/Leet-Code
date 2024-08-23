class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;

        unordered_map<int, int> numMap;
        for(const auto& i : nums){
            numMap[i] += 1;
        }

        typedef pair<int, int> p1;
        priority_queue<p1, vector<p1>, greater<p1>> min_heap;
        for(const auto& i : numMap){
            min_heap.push(make_pair(i.second, i.first));
            if(min_heap.size() > k){
                min_heap.pop();
            }
        }

        while(!min_heap.empty()){
            pair<int, int> p = min_heap.top();
            min_heap.pop();
            result.push_back(p.second);
        }

        return result;
    }
};