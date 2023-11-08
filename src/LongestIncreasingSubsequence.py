"""

Given an int array return the length of longest strictly increasing subsequence
"""


#Dynamic Programming solution -> O(n**2) - time O(n) - size
def lengthOfLIS( N) -> int:

    dp = [1]*len(N) #initializing dp  where dp[i] : size of LIS that ends with N[i]

    #relation : dp[i] = max(dp[j] + 1) 

    for i in range(1,len(N)):
        k = []
        print(f"k: {k}")

        dp[i] = max([(dp[j] + 1 ) if N[j]<N[i] else 1 for j in range(0,i)])

        print(f"dp : {dp}")


    return max(dp)


# Build intelligent subsequence soln: O(n**2) ->can improve if we replace linear search with binary search

def lengthOfLIS(N: list[int]) -> int:


    def linear_search(nums,to_find):

        for i in range(len(nums)):

            if nums[i]>= to_find:

                return i

        return -1


    lis = [N[0]]

    for i in range(len(N)):

        if N[i] > lis[-1]:

            lis.append(N[i])
            # print(F"lis simple add : {lis}")


        else:
            print(f"need to choose")

            to_replace = linear_search(lis,N[i])

            if to_replace != -1:

                lis[to_replace] = N[i]

                # print(f"lis  {lis[to_replace]} replaced ,new lis : {lis}")

    # print(lis)
    return len(lis)






#Brute Force solution --> wrong not taking care of all casess

def lengthofLIS_(N):

    hash = {}

    for i in range(0,len(N)):
        subarray = [N[i]]
        for j in range(i+1,len(N)):

            if N[j] > N[i] and N[j] > subarray[-1]:
                subarray.append(N[j])
                print(f"{N[j]} > {N[i]}")

                
        print(f"subarray: {subarray}")

        hash[i]= len(subarray)
    print(hash)


    return max(hash.values())


if __name__ == "__main__":

    # nums = [0,1,0,3,2,3]
    # nums = [10,9,2,5,3,7,101,18]
    # nums = [7,7,7,7,7,7,7]
    nums= [4,10,4,3,8,9]
    # nums =  [0,1,0,3,2,3]
    # 
    print(lengthOfLIS(nums))