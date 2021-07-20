from collections import Counter
class Solution:
    """
    @param str: a string for calculating.
    @param k: the length of special substring.
    @return: return the number of special substrings.
    """
    def specialSubstringCount(self, S, K):
        # write your code here.
        '''
        helloo k = 4
        '''
        # cnt = {}
        # l = list(str)
        # cnt = collections.Counter(l[:k])
        # for n in cnt:
        #     if cnt[n] > 1:
        #         special_str = 1
        # for i in range(len(l) - k):
        #     cnt[l[i]] -= 1:
        char_to_count = Counter()
        num_repeated = 0
        answer = 0
        for i in range(len(S)):
            if i < K:
                char_to_count[S[i]] += 1 
                if char_to_count[S[i]] == 2:
                    num_repeated += 1 
            else:
                if num_repeated == 1:
                    answer += 1         
                char_to_count[S[i]] += 1  
                if char_to_count[S[i]] == 2:
                    num_repeated += 1
                char_to_count[S[i - K]] -= 1 
                if char_to_count[S[i - K]] == 1:
                    num_repeated -= 1
        if num_repeated == 1:
            answer += 1
        return answer
        