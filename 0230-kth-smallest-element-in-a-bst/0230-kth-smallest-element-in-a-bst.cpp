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
    int kthSmallest(TreeNode* root, int k) {
        if(k<1){
            return 0;
        }
        vector<int> v;
        inorder(root,v);
        return v.at(k-1);
    }
    void inorder(TreeNode* root, vector<int>& L){
        if(root == nullptr){
            return;
        }
        inorder(root->left,L);
        L.push_back(root->val);
        inorder(root->right,L);
    }
};