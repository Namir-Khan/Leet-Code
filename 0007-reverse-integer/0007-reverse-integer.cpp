class Solution {
public:
    int reverse(int x) {
        int sign = (x < 0) ? -1 : 1;
        x = abs(x);
        int rev = 0;
        while(x > 0){
            int k = x % 10;
            x /= 10;
            if (rev > (INT_MAX - k) / 10) {
                return 0;
            }
            rev = (rev * 10) + k;
        }
        return rev*sign;
    }
};