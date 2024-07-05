# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or
#  phrase, typically using all the original letters exactly once.
from collections import defaultdict
def ValidAnagram(s,t):
    anagram_map= defaultdict(list)
    sorted_s = sorted(s)
    anagram_map[s].append(sorted_s)
    sorted_t = sorted(t)
    anagram_map[t].append(sorted_t)
    if anagram_map[t] == anagram_map[s]:
        return True
    else:
        return False

    