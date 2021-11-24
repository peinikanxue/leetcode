/*
 * @lc app=leetcode.cn id=563 lang=cpp
 *
 * [563] 二叉树的坡度
 */


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// @lc code=start
#include <cstdlib>
#include <queue>

class Solution {
public:
    int findTilt(TreeNode* root) {
        if(root == nullptr)
            return 0;
        postTree(root);
        levelTree(root);
        postTree(root);
        return root->val;
    }

    int postTree(TreeNode* root){
        if(root == nullptr)
            return 0;

        return root->val += postTree(root->left) + postTree(root->right);
    }

    void levelTree(TreeNode* root){
        std::queue<TreeNode*> Q;
        if(root != nullptr)
            Q.push(root);

        int left = 0, right = 0;
        TreeNode* tmp;
        while(not Q.empty()){
            tmp = Q.front();
            Q.pop();
            left = tmp->left == nullptr ? 0 : tmp->left->val;
            right = tmp->right == nullptr ? 0 : tmp->right->val;
            tmp->val = abs(left - right);

            if(tmp->left != nullptr)
                Q.push(tmp->left);
            if(tmp->right != nullptr)
                Q.push(tmp->right);
        }
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    TreeNode root(4);
    TreeNode node2(2);
    TreeNode node9(9);
    TreeNode node3(3);
    TreeNode node5(5);
    TreeNode node7(7);

    root.left = &node2;
    root.right = &node9;

    node2.left = &node3;
    node2.right = &node5;

    node9.right = &node7;

    Solution().findTilt(nullptr);
    /* code */
    return 0;
}

/*
Your runtime beats 98.38 % of cpp submissions
Your memory usage beats 8.59 % of cpp submissions (23.4 MB)

time: O(n)
space: O(1)
*/

/*
后序遍历 + 层序遍历
*/