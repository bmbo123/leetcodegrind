class Solution {
public:
    bool is_number(const string& s) {
        return !s.empty() && (isdigit(s[0]) || (s[0] == '-' && s.size() > 1));
    }
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for (int i = 0; i < tokens.size(); i++) {
            string ch = tokens[i];
            if (is_number(ch)) {
                st.push(stoi(ch));
            } else {
                int a = st.top();
                st.pop();
                int b = st.top();
                st.pop();
                if (ch == "+") {
                    int c = b + a;
                    st.push(c);
                }
                if (ch == "-") {
                    int c = b- a;
                    st.push(c);
                }
                if (ch == "*") {
                    int c = b*a;
                    st.push(c);
                }
                if (ch == "/") {
                    int c = b/a;
                    st.push(c);
                }
            }
        }
        return st.top();
    }
};