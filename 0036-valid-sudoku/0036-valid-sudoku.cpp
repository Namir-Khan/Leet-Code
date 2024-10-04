class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, int> row[9];
        unordered_map<int, int> col[9];
        unordered_map<int, int> box[9];
        
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                if(board[i][j] != '.') {
                    int num = board[i][j] - '0';
                    
                    if(row[i][num] == 1) {
                        return false;
                    } 
                    else {
                        row[i][num] = 1;
                    }
                    
                    if(col[j][num] == 1) {
                        return false;
                    } 
                    else {
                        col[j][num] = 1;
                    }

                    int boxIndex = (i / 3) * 3 + (j / 3);
                    
                    if(box[boxIndex][num] == 1) {
                        return false;
                    } 
                    else {
                        box[boxIndex][num] = 1;
                    }
                }
            }
        }
        return true;
    }
};