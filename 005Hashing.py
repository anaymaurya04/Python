#Hashmap/ Dictionaries
from collections import defaultdict
std_id=defaultdict(list)
name = ["Anay", "Aditya", "Sarthak", "Yash", "Shaswat"]
std_id["310"] += name

#49 Group Anagrams(Medium)
#242 Valid Anagrams(Easy)
#GFG-Frequency
def freq(arr,N,p):
    freq_map = {}
    for i in arr:
        if 1 <= i <= N:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1
    for i in range(1, N + 1):
        arr[i - 1] = freq_map.get(i, 0)

