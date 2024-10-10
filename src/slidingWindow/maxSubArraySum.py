def maxSubarraySum(arr,k):

    N = len(arr)
    p1 = p2 = 0
    max_sum = sum = 0
    while p2 < N:  #dont need to check p1 because p1 will always be k less than p2, therefore it wont reach N before p2

        sum = sum + arr[p2]

        if p2 - p1 + 1 < k:
            p2+=1

        elif (p2 - p1 + 1) == k:
            max_sum = max(sum,max_sum)
            sum = sum - arr[p1]
            p1+=1
            p2+=1

    return max_sum


if __name__ == '__main__':
    arr = [2,5,1,8,2,9,1]
    k = 2
    print(f"max sum for subarray of {k} = {maxSubarraySum(arr,k)} ")
