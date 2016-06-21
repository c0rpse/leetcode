//
//  274. H-Index.hpp
//  leetcode
//
//  Created by c0rpse on 16/6/20.
//  Copyright © 2016年 c0rpse. All rights reserved.
//

#ifndef _74__H_Index_hpp
#define _74__H_Index_hpp
#include <vector>

using namespace std;
class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(),citations.end());
        int h = 0;
        for(auto i = citations.rbegin();i!=citations.rend();++i){
            if(*i >= h) ++h;
            else break;
        }
        return h;
    }
};
#include <stdio.h>

#endif /* _74__H_Index_hpp */
