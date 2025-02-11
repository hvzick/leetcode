nums = [4,1,-1,2,-1,2,3]
k = 2
# d = {}
# o = []
# # for i in range(0, len(nums)):
# #     if nums[i] == nums[i-1]:
# #         count += 1
# #         o.append(count)
# #     if not nums[i] == nums[i-1]:
# #         count = 0

# # print(o)

# for i in nums:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1




# si = sorted(d.items(), key=lambda item: item[1], reverse=True)
# sd = dict(si)
    

# for i,j in sd.items():
#     o.append(i)

# print(o[0:k])

# # for i in nums:
# #     if nums[i] == nums[i-1]:
# #         d[i] = 

# # for i in range(0, len(nums)):
# #     if d[i] == d[i+1]:
# #         d[i] = d[i] + 1


def topKFrequent(nums, k):
    d = {}
    o = []
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 0            
    si = sorted(d.items(), key=lambda item: item[1])
    sd = dict(si) 
    for i,j in sd.items():
        o.append(i)
    
    return o[-k:]

x = topKFrequent(nums,k)
print(x)    