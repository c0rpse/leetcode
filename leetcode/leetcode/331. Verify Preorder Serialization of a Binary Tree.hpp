//
//  331. Verify Preorder Serialization of a Binary Tree.hpp
//  leetcode
//
//  Created by c0rpse on 16/6/20.
//  Copyright © 2016年 c0rpse. All rights reserved.
//

#ifndef _31__Verify_Preorder_Serialization_of_a_Binary_Tree_hpp
#define _31__Verify_Preorder_Serialization_of_a_Binary_Tree_hpp

#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    vector<string> isValidSerialization(string preorder) {
//        if(preorder.size() == 0) return ;
        vector<string> v = split(preorder, ",");
        
        return v;
    }
private:
    vector<string> split(const string &preorder,const string &flag){
        vector<string> ret;
        size_t pos = preorder.find(flag),cur_pos = 0;
        while (cur_pos != preorder.npos) {
            ret.push_back(preorder.substr(cur_pos,pos - cur_pos -1));
            if(pos == preorder.npos)
                cur_pos = pos;
            else{
                cur_pos = pos + 1;
                pos = preorder.find(flag,cur_pos);
            }
        }
        return ret;
    }
};
#endif /* _31__Verify_Preorder_Serialization_of_a_Binary_Tree_hpp */
