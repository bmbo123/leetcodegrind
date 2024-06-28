class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int i = 0;
        int j = 0;
        while (j < typed.length()) {
            if (i < name.length() && name[i] == typed[j]) {
                i++;
                j++;
            } else if (i > 0 && typed[j] == name[i - 1]) {
                j++;
            } else {
                return false;
            }
        }
        return i == name.length();
    }
};
