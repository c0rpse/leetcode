//
//  80. Remove Duplicates from Sorted Array II.h
//  leetcode
//
//  Created by c0rpse on 16/6/16.
//  Copyright © 2016年 c0rpse. All rights reserved.
//

#ifndef _0__Remove_Duplicates_from_Sorted_Array_II_h
#define _0__Remove_Duplicates_from_Sorted_Array_II_h
#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_map<int,int> map;
        int sum = 0;
        for(auto i = nums.begin();i!=nums.end();++i){
            if(map.find(nums[i]) != map.end()) map[nums[i]] += 1;
            else map[nums[i]] = 1;
        }
        for(auto i = map.begin();i!=map.end();++i){
            if((*i).second<3) sum += (*i).second;
            else sum += 2;
        }
        return sum;
    }
};
#endif /* _0__Remove_Duplicates_from_Sorted_Array_II_h */
