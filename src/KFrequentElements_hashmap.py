from collections import Counter

def topKFrequent(self, nums, k: int) -> list[int]:
    
    #make a hash map with frequency of each number
    counts_dict = Counter(nums)
    
    #sort th hash map wrt the frequence
    sorted_dict = dict(sorted(counts_dict.items(), key=lambda item: item[1])) #if we use item[0] it will sort w.r.t. the key right now sorting w.r.t. values for keys

    #print the sorted dict
    
    #print("a",sorted_dict)

    
    #print("elements in increasing order of their frequency: ",list(sorted_dict.keys()))
    
    return list(sorted_dict.keys())[(-1)*k:]
        

        