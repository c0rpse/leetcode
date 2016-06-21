//
//  78. Subsets.hpp
//  leetcode
//
//  Created by c0rpse on 16/6/20.
//  Copyright © 2016年 c0rpse. All rights reserved.
//

#ifndef _8__Subsets_hpp
#define _8__Subsets_hpp

#include <iosteam>
#include <vector>

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> sets;
        vector<int> cur;
        sets.push_back(cur);
        int s = nums.size();
        if(!s) return sets;
        sort(nums.begin(),nums.end());
        
        for(int k=1;k<=s;++k){
            vector<int> sum;
            dfs(sets,sum,nums,0,k);
        }
        return sets;
    }
private:
    void dfs(vector<vector<int>> &sets,vector<int> &cur_set,vector<int> &source ,int start,int k){
        if(cur_set.size() == k) {sets.push_back(cur_set);return;}
        int s_size = source.size();
        for(int i = start;i< s_size;++i){
            //回溯
            cur_set.push_back(source[i]);
            dfs(sets,cur_set,source, i+1,k);
            cur_set.pop_back();
        }
    }
};

#endif /* _8__Subsets_hpp */
