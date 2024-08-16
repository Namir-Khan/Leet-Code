class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> strMap;
        for ( const string& i : strs){
            string temp = i;
            sort(temp.begin(), temp.end());
            strMap[temp].push_back(i);
        }

        vector<vector<string>> result;
        for (const auto& pair : strMap){
            result.push_back(pair.second);
        }

        return result;
    }
};