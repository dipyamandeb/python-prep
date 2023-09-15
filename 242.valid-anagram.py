#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMapS = {}
        countMapT = {}
        if len(s)!=len(t):
            return False 
        for i in range(len(s)):
            countMapS[s[i]] = 1+countMapS.get(s[i],0)
            countMapT[t[i]] = 1+ countMapT.get(t[i],0)

        return countMapS==countMapT  
        
# @lc code=end

