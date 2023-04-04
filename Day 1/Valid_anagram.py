class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

    # Basic Idea: Take it as set and then compare them?
        # s_set = set()
        # count = 0
        # for i in s:
        #     s_set.add(i)
        # for j in t:
        #     if j in s_set:
        #         print(j)
        #         count = count+1
        #     else:
        #         s_set.add(j)
        # print(count)
        # if(len(s) == len(t)):
        #     if(count == len(t)):
        #         return True
        # else:
        #     return False

        #it doesnt work lol
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(freq)):
            if freq[i] != 0:
                return False
        
        return True