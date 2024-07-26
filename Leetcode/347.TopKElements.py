class Solution(object):
    def topKFrequent(self, nums, k):
        count_map= {}
        freq_bucket=[[]for i in range (len(nums)+1)]
        for num in nums:
            if num in count_map:
                count_map[num] +=1
            else:
                count_map[num] = 1
        for num,c in count_map.items():
            freq_bucket[c].append(num)
        res = []
        for i in range(len(nums),0,-1):
            for num in freq_bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
        
        