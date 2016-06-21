//
//  33. Search in Rotated Sorted Array.hpp
//  leetcode
//
//  Created by c0rpse on 16/6/20.
//  Copyright © 2016年 c0rpse. All rights reserved.
//

#ifndef _3__Search_in_Rotated_Sorted_Array_hpp
#define _3__Search_in_Rotated_Sorted_Array_hpp

#include <stdio.h>
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(!nums.size()) return -1;
        size_t left = 0,right = nums.size()-1,mid;
        while (left <= right) {
            mid = left + (right-left)/2;
            if(nums[mid] == target) return mid;
            else if(nums[mid] < target){
                
            }
        }
    }
};

#endif /* _3__Search_in_Rotated_Sorted_Array_hpp */
