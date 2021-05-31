# !/usr/bin/env python
# coding: utf-8

"""
Description: 各种子串的题目及解法
Authors: wuruonan
Date: 2021/5/31
"""


class SubString(object):
    def __init__(self):
        pass


class LengthOfLongestSubstringWithoutRepitation(SubString):
    """
    无重复字符的最长子串: 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    输入：  字符串，如 abcabcbb/bbbbb/pwwkew
    输出：  不含重复字符的最长子串的长度，如3/1/3
    """
    @classmethod
    def sliding_window(cls, string):
        """
        解法：滑动窗口
        leetcode: 48ms/13.5MB
        1. 定义窗口两端begin、end，分别标识子串的开头、结尾
        2. 以abcabcbb为例，开始的时候begin和end都指向0即a
        3. 然后end不断后移
        4. 直到遇到第二个a时，得到一个子串，及长度（end和begin的位置差）
        5. begin此时应当指向第一个a后面的位置，即b，计算以b开头的最长子串
        6. 子串之间比较，获取最大长度
        """
        maxlen = 0
        temp_dict = dict()
        begin, end = 0, 0
        length = len(string)
        while end < length:
            last_index = temp_dict.get(string[end])
            temp_dict[string[end]] = end  # 字典key:value为值：索引（a:1）
            if last_index is not None:  # 出现了重复的情况
                maxlen = max(maxlen, end-begin)  # 比较当前未重复子串与最大长度
                begin = max(begin, last_index + 1)  # 获取下次的起始索引
                #####  什么时候begin> last_index+1?
            end += 1

        maxlen = max(maxlen, end-begin)
        return maxlen

    @classmethod
    def simple_solution(cls, string):
        """
        暴力求解
        leetcode： 4680ms/ 15.1MB
        """
        if len(string) <= 1:
            return len(string)
        list_str = list(string)
        sub_str = ''
        for i in range(0, len(list_str)):
            tmp_str = ''
            for j in range(i, len(list_str)):
                if list_str[j] not in tmp_str:
                    tmp_str += '{0}'.format(list_str[j])
                else:
                    break
            if len(tmp_str) > len(sub_str):
                sub_str = tmp_str
        return len(sub_str)


if __name__ == '__main__':
    str = 'abcabcaa'
    print LengthOfLongestSubstringWithoutRepitation.simple_solution(str)
    str = 'bbbbbb'
    print LengthOfLongestSubstringWithoutRepitation.simple_solution(str)
    str = 'pwwkew'
    print LengthOfLongestSubstringWithoutRepitation.simple_solution(str)
    str = ''
    print LengthOfLongestSubstringWithoutRepitation.simple_solution(str)



