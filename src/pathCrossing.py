"Return true if paths crossed in a given string"

#Using Hash Table


def isPathCrossing( path: str):

    map = {
        "N":(0,+1),
        "S":(0,-1),
        "E":(1,0),
        "W":(-1,0)
    }

    x,y =0 ,0

    visited = [(0,0)]

    for direction in path:

        dx = map[direction][0]
        dy = map[direction][1]

        x+=dx
        y+=dy

        if (x,y) in visited:
            return True

        else:
            visited.append((x,y))








#Very basic, redundant variables solution - O(n) - time


def isPathCrossing(path: str) -> bool:

    points_visited = []
    x_now = 0
    y_now = 0
    point_now = (x_now,y_now)
    points_visited.append(point_now)

    
    for i in range(len(path)):

        if path[i] == "N":

            y_now+=1
            point_now = (x_now,y_now)
            # print(f"current_point : {point_now}")
            points_visited.append(point_now)

            if len(set(points_visited)) < 2+i:
                return True

        elif path[i] == "S":

            y_now-=1
            point_now = (x_now,y_now)
            # print(f"current_point : {point_now}")
            points_visited.append(point_now)

            if len(set(points_visited)) < 2+i:
                return True

        elif path[i] == "E":

            x_now+=1
            point_now = (x_now,y_now)
            points_visited.append(point_now)

            if len(set(points_visited)) < 2+i:
                return True

        else:

            x_now-=1
            point_now = (x_now,y_now)
            points_visited.append(point_now)

            if len(set(points_visited)) < 2+i:
                return True

    return False
    

if __name__ == "__main__":

    assert isPathCrossing("NES") == False
    assert isPathCrossing("NESWW") == False,"Wrong output"