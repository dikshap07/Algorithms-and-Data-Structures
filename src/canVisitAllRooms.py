def canVisitAllRooms(rooms):

    visited = [False]*len(rooms)

    stack = [0]
    visited[0] = True

    while stack:

        key = stack.pop()

        for key in rooms[key]:

            if visited[key] == False:

                stack.append(key)
                visited[key] = True

    return all(visited)


if __name__ == "__main__":

    rooms =[ [0],[1]]
    # [[1,3],[3,0,1],[2],[0]]
    # [[1],[2],[3],[]]

    print(canVisitAllRooms(rooms))