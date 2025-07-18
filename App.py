# # RELATIVE RANK
# def findRelativeRanks(score):
#     sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
#     ranks = [""] * len(score)

#     for i, (index, _) in enumerate(sorted_scores):
#         if i == 0:
#             ranks[index] = "Gold Medal"
#         elif i == 1:
#             ranks[index] = "Silver Medal"
#         elif i == 2:
#             ranks[index] = "Bronze Medal"
#         else:
#             ranks[index] = str(i + 1)

#     return ranks

# score = [10, 3, 8, 9, 4]
# result = findRelativeRanks(score)
# print(result)


# VALID ANAGRAM

# def is_anagram(s, t):
#     if len(s) != len(t):
#         return False
#     return sorted(s) == sorted(t)

# s = "listen"
# t = "silent"
# print(is_anagram(s, t))  

# s = "stop"
# t = "past"
# print(is_anagram(s, t)) 


# MAXIMUM GAP
def maximumGap(nums):
    if len(nums) < 2:
        return 0
    
    min_val, max_val = min(nums), max(nums)
    
    bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))  #
    
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    
    for num in nums:
        idx = (num - min_val) // bucket_size
        buckets[idx].append(num)
    
    max_gap = 0
    prev_max = min_val
    
    for bucket in buckets:
        if bucket:  
            current_min = min(bucket)
            max_gap = max(max_gap, current_min - prev_max)
            prev_max = max(bucket)
    
    return max_gap
nums = [3, 6, 9, 1]
print(maximumGap(nums)) 

