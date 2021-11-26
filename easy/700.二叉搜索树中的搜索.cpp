/*
 * @lc app=leetcode.cn id=700 lang=cpp
 *
 * [700] 二叉搜索树中的搜索
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// @lc code=start
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
    TreeNode* searchBST(TreeNode* root, int val) {
        if(val == root->val)
            return root;
        
        TreeNode* tmp;
        if(root->left and (tmp = searchBST(root->left, val)))
            return tmp;
        if(root->right and (tmp = searchBST(root->right, val)))
            return tmp;
        return nullptr;
    }
};
// @lc code=end

/*
36/36 cases passed (32 ms)
Your runtime beats 88.53 % of cpp submissions
Your memory usage beats 31.21 % of cpp submissions (34 MB)

time: O(n)
space: O(n)

不是搜索二叉树，需要全部遍历。
*/