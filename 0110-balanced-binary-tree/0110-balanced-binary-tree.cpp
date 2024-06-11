/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    // Condition - Take & of them
    // 1 - left subtree balanced
    // 2 - right subtree balanced
    // 3 - L.H - R.H <= 1

    // BC = when root is NULL return true
    // TC = O(N*N), because calculating height for each node

    // int height(TreeNode *root)
    // {
    //     if (root == NULL)
    //     {
    //         return 0;
    //     }

    //     int l = 1 + height(root->left);
    //     int r = 1 + height(root->right);
    //     return max(l, r);
    // }

    // bool isBalanced(TreeNode* root) {
    //     if(root == NULL){
    //         return true;
    //     }

    //     int leftheight = height(root->left);
    //     int rightheight = height(root->right);

    //     if(abs(leftheight - rightheight ) > 1){
    //         return false;
    //     }

    //     bool leftAns = isBalanced(root->left);
    //     bool rightAns = isBalanced(root->right);
        
    //     return (leftAns && rightAns);
        
    // }


    // Method 2 - faster way TC = O(N)
    // keep track while calculating height

    int height(TreeNode *root, bool &ans)
    {
        if (root == NULL)
        {
            return 0;
        }

        int l = height(root->left,ans);
        int r = height(root->right,ans);

        // find if not balanced
        if(abs(l-r) > 1){
            ans = false;
        }
        return max(l, r) + 1;
    }

    bool isBalanced(TreeNode* root) {
        if(root == NULL){
            return true;
        }

        bool ans = true;
        height(root,ans);
        return ans;
    }
};