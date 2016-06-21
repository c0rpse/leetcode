//
//  129. Sum Root to Leaf Numbers.hpp
//  leetcode
//
//  Created by c0rpse on 16/6/16.
//  Copyright © 2016年 c0rpse. All rights reserved.
//

#ifndef _29__Sum_Root_to_Leaf_Numbers_hpp
#define _29__Sum_Root_to_Leaf_Numbers_hpp

#include <stdio.h>
#include <vector>

using namespace std;

struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if(!root) return 0;
        int sum = 0;
        part(root,0,sum);
        return sum;
    }
private:
    void part(TreeNode* root,int preSum,int &sum){
        if(!root) return;
        if(root->left == NULL && root->right == NULL){
            sum += preSum*10 + root->val;
        }
        else{
            if(root->left) part(root->left,preSum*10 + root->val,sum);
            if(root->right) part(root->right,preSum*10 + root->val,sum);
        }
    }
};

#endif /* _29__Sum_Root_to_Leaf_Numbers_hpp */
