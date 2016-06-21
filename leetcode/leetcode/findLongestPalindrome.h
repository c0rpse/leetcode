//
//  findLongestPalindrome.h
//  leetcode
//
//  Created by c0rpse on 16/6/16.
//  Copyright © 2016年 c0rpse. All rights reserved.
//

#ifndef findLongestPalindrome_h
#define findLongestPalindrome_h

using namespace std;
class Solution{
public:
string findLongestPalindrome(string &s){
    const int s_size = s.size();
    bool p[s_size][s_size] = {false};
    int start = 0, max_length = 0;
    for(int i = 0;i<s_size;++i){
        p[i][i] = true;
        if(i < s_size - 1 && s.at(i) == s.at(i+1)){
            p[i][i+1] = true;
            start = i;
            max_length = 2;
        }
    }
    for(int len = 3;len < s_size;++len){
        for(int i = 0;i<=s_size - len;++i){
            int j = i+len-1;
            if[(p[i+1][j-1] == 1 && s.at(i) == s.at(j)){
                p[i][j] = true;
                start = i;
                max_length = len;
            }
        }
    }
               if(max_length > 2) return s.substr(start,max_length);
               return NULL;
}
            }
#endif /* findLongestPalindrome_h */
