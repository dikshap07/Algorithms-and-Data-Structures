from collections import defaultdict
import heapq

"""Priority Queue implementation"""


def highFive(items):
    id_scores = defaultdict(list)

    for (
        id,
        score,
    ) in items:  # O(n) times loop runs for n ids,n times  O(log 5 )heap operations
        # total = O(nlog5) complexity

        # add to heap for each id
        heapq.heappush(id_scores[id], score)  # id_scores[id] : heap for id

        if len(id_scores[id]) > 5:  # if len(heap) > 5, we start popping to get max 5
            heapq.heappop(id_scores[id])

        print(f" Heap for id: {id} is {id_scores[id]}")

    res = [
        [id, sum(id_scores[id]) // 5] for id in sorted(id_scores.keys())
    ]  # O(n) for n ids the loop runs, O(nlogn) to sort the dictionary
    # Total = O(n) + O(nlogn)
    return res


"""Using hashmap and sorting"""


def highFive(items):
    id_scores = defaultdict(list)
    min_scores = {}
    # max_scores = {}

    for id, score in items:
        """
        Currently using min() to get top5, should use maxHeap.
        """

        # print(f"{id} : {score}")

        if id in id_scores:
            # print(f"id: {id} in id_scores")

            if len(id_scores[id]) < 5:
                # print("here")

                id_scores[id].append(score)
                if score <= min_scores[id]:
                    # print("<=")
                    min_scores[id] = score
                continue

            if len(id_scores[id]) >= 5:
                # check if currenr score is greater than min

                if score > min_scores[id]:
                    id_scores[id].remove(min_scores[id])
                    id_scores[id].append(score)
                    min_scores[id] = min(id_scores[id])

        if id not in id_scores:  # if new id found
            # print(f"id: {id} not in id_scores")

            min_scores[id] = score
            # max_scores[id] = score
            id_scores[id].append(score)

        # print(f"id_scores[{id}]: {id_scores[id]}")
        # print(f"id {id} minscore = {min_scores[id]}")

    """
    
    this while loop and using min() is not a good choice, need to optimize it

    """
    res = []

    while len(list(id_scores)) != 0:
        min_id = min(id_scores.keys())
        res.append([min_id, sum(id_scores[min_id]) / 5])
        id_scores.pop(min_id)

    print(res)

    return id_scores


if __name__ == "__main__":
    items = [
        [2, 77],
        [1, 91],
        [1, 92],
        [2, 93],
        [2, 97],
        [1, 60],
        [1, 65],
        [1, 87],
        [1, 100],
        [2, 100],
        [2, 76],
    ]
    # items = [
    #     [1, 100],
    #     [7, 100],
    #     [1, 100],
    #     [7, 100],
    #     [1, 100],
    #     [7, 100],
    #     [1, 100],
    #     [7, 100],
    #     [1, 100],
    #     [7, 100],
    # ]

    print(highFive(items))
