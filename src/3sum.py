def twosum_sorted(nums,i,res):

    left = i+1
    right = len(nums)-1

    curr_sum = nums[i] + nums[left] + nums[right]

    while left < right:
        if curr_sum < 0:

            left+=1

        elif curr_sum > 0:
            right-=1

        else:

            res.append([nums[i],nums[left],nums[right]])
            left+=1
            right-=1

            while left < right and nums[left] == nums[left-1]:
                left+=1

def twosum_set(nums,i,res):

    seen = set()#still need to sort the array

    j = i+1

    while j+1  < len(nums)-1:

        complement = -nums[i]-nums[j] #complement

        if complement in seen:
            j+1
            res.append([nums[i],nums[j],complement])

            while j+1< len(nums)-1 and nums[j+1]==nums[j]:
                j+=1

        seen.add(nums[j])
        j+=1




def threesum(nums):

    nums.sort() #sort the array
    res = []
    for i in range(len(nums)):

        if nums[i] > 0: #because sorted and if the curr num is greater than 0 then we wont find nums on right to make the sum 0
            break
        
        if i == 0 or nums[i-1] != nums[i]: #if the last num is not same as the current we seach for the twosum pair

            twosum_sorted(nums,i,res)

    return res


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(threesum(nums))


#failed -> two complicated attempt: works but doesnt give unique values-> repeats answers


# def twosum(nums,target_sum,current_index):
#     index_hash ={}
#     for i in range(len(nums)):

#         index_hash[nums[i]] = i

#     pairs = []
#     index_pairs = []

#     for num in index_hash.keys():
        
#         target_num = target_sum - num
#         if target_num in index_hash.keys() and index_hash[num] != index_hash[target_num] and index_hash[num] != current_index and index_hash[target_num] != current_index:
            

#             if ((index_hash[num],index_hash[target_num]) not in index_pairs) and ((index_hash[target_num],index_hash[num]) not in index_pairs):
#                 pairs.append([num,target_num])
#                 index_pairs.append((index_hash[num],index_hash[target_num]))
#             # print(f"pairs at num= {num}: {pairs}")

#     return pairs

# #build index_hash

# res = {}
# for i in range(len(nums)):
#     res_ = []
#     print(f" set(nums) : {set(nums)}")
#     print(f"nums: {nums}")
#     nums2 = list(nums)       
#     two_pairs = twosum(nums2,nums[i]*(-1),i)

#     print(f"opp sum pairs for {nums[i]} : {two_pairs}")

#     for pair in two_pairs:
#         print(f"pair: {pair}")
#         pair.append(nums[i])
#         print(f"triplet for {nums[i]} : {pair}")
#         res_.append(pair)

#     if nums[i] not in res.keys():

#         res[nums[i]] = res_
    

#     print(f"res for {nums[i]}: {res}")