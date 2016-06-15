//
//  279. Perfect Squares.hpp
//  leetcode
//
//  Created by c0rpse on 16/6/15.
//  Copyright © 2016年 c0rpse. All rights reserved.
//

#ifndef _79__Perfect_Squares_hpp
#define _79__Perfect_Squares_hpp

#include <vector>
using namespace std;
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1,0);
        for(int i=0;i<n+1;i++)
            dp[i]=i;  //最多都由1组成
        for(int i=0;i<=n;i++)
            for(int j=1;i+j*j<=n;j++)
                dp[i+j*j]=min(dp[i+j*j],dp[i]+1);//要么本身，要么加一个平方数
        
        return dp[n];
    }
};

#endif /* _79__Perfect_Squares_hpp */
