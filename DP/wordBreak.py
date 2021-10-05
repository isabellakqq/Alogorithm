# Code & Idea for questions :

# Word Break : Ques No. 139
# Word Break II : Ques No. 140
# Concatenated Words : Ques No. 472
# Basic idea is same for all, find if string can be broken down to smaller string. Word Break I template follows other two.

# Word Break I
# Using dynamic programming to calculate if word break is possible or not

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         dp = [False] * (len(s) + 1)
#         dp[0] = True
#         wordDict = set(wordDict)
        
#         for i in range(len(s)+1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in wordDict:
#                     dp[i] = True
#         return dp[-1]
# Word Break II
# This is backtracking plus dynamic programming. We use dp array generated from word break I to figure out remaining string can be splitted or not, this reduces lot of backtracking calls.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return [""]
        
        self.res = []
        self.wordDict = set(wordDict)
        self.dp = self.isWordBreak(s, wordDict)
        self.backtrack(s, 0, [])
        
        return self.res
    
    def backtrack(self, s, idx, path):
        # Before we backtrack, we check whether the remaining string 
        # can be splitted by using the dictionary,
        # in this way we can decrease unnecessary computation greatly.
        if self.dp[idx+len(s)]: # if word break possible then only proceed
            if not s:
                self.res.append(' '.join(path))
            else:
                for i in range(1, len(s)+1):
                    if s[:i] in self.wordDict:
                        self.backtrack(s[i:], idx+i, path + [s[:i]])
        
    # this is from Word Break I
    def isWordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp
# Concatenated Words
# Concatenated Words is the reverse of Word Break I, so can be broken down to Word Break I.

# Sort the words according to shortest length since short ones form long words
# for each word start building our dictionary of words and check if word split is possible or not
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        preWords = set()
        
        # asc order of word length, since longer words are formed by shorter words
        words.sort(key = len)
        
        # for each short word start building preWords
        for word in words:
            if self.wordBreak(word, preWords):
                res.append(word)
            preWords.add(word)
        
        return res
    
    # Word Break I template
    def wordBreak(self, string, words):
        if not words:
            return False
        
        dp = [False] * (len(string) + 1)
        dp[0] = True
        
        for i in range(len(string)+1):
            for j in range(i):
                if dp[j] and string[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]