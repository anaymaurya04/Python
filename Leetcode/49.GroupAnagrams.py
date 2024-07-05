# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
from collections import defaultdict
strs = ["eat","tea","tit","itt"]
anagram_map =defaultdict(list)
result = []
for s in strs:
    sorted_s = tuple(sorted(s))
    anagram_map[sorted_s].append(s)
    
for values in anagram_map.values():
    result.append(values)

print(result)