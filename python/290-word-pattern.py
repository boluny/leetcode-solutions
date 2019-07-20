# -*- coding: utf-8 -*-

class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        if not pattern or not string:
            return False
        
        words = string.split()
        if len(pattern) != len(words):
            return False
        
        map_string = {}
        map_pattern = {}
        for i, letter in enumerate(pattern):
            # we add to dict if we see the link between letter and word in the first time
            # make it as an base dictionary for subsequence lookup
            if not map_string.get(letter):
                # reverse link to ensure words can't be mapped to different letter
                if not map_pattern.get(words[i]):
                    map_string[letter] = words[i]
                    map_pattern[words[i]] = letter
                elif map_pattern.get(words[i]) != letter:
                    return False
            else:
                if map_string[letter] != words[i]:
                    return False
                
        return True

def test_solution():
    ss = Solution()

    assert ss.wordPattern('abba', 'dog cat cat dog') == True
    assert ss.wordPattern('abba', 'dog cat cat fish') == False
    assert ss.wordPattern('aaaa', 'dog cat cat dog') == False
    assert ss.wordPattern('abba', 'dog dog dog dog') == False