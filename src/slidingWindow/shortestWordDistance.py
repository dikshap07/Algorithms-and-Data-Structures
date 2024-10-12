def shortestWordDistance(arr,w1,w2):


    min_dist = 300000

    p1 = 0
    p2 = 0


    while p1 < len(arr) or p2< len(arr):

        if arr[p1] == w1:
            idx1 = p1
            # p1+=1
            #if w1 found, lets look for w2 keeping w1 first index
            while p2 < len(arr):

                if arr[p2] == w2:

                    idx2 = p2

                    min_dist = min(min_dist,abs(idx2-idx1))
                    #if we found w2 break out of this loop and find w1 again
                    p1+=1
                    break

                else:
                    p2+=1

        else:
            p1+=1

    return min_dist



arr = ["practice", "makes", "perfect", "coding", "makes"]

shortestWordDistance(arr,"coding", "makes")