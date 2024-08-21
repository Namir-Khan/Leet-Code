class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> heap;
        int n = stones.size();

        for(int i = 0; i < n; i++){
            heap.push(stones[i]);
        }

        int first,second;
        while(n>1){
            first = heap.top();
            heap.pop();
            second = heap.top();
            heap.pop();
            n -= 2;

            if(first-second > 0){
                heap.push(first-second);
                n += 1;
            }
        }

        if(!heap.empty()){
            return heap.top();
        }
        return 0;
    }
};