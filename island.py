island_map = [
        [1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0]
      ]


def is_next_to(island_map, x1, y1, x2, y2):
    if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
        return False
    if x1 + 1 == x2 and y1 == y2:
        return True
    elif x1 - 1 == x2 and y1 == y2:
        return True
    elif y1 + 1 == y2 and x1 == x2:
        return True
    elif y1 - 1 == y2 and x1 == x2:
        return True
    return False


def island(map):
    count = 0
    x = 0
    y = 0
    max_x = len(map[0])
    max_y = len(map)
    land = []
    for i in range(max_x * max_y):
        if x+1 == max_x:
            y += 1
            x = 0
        if map[y][x] == 1:
            is_in_land = False
            for i in land:
                if is_next_to(map, x, y, i[0], i[1]):
                    map[y][x] = map[i[1]][i[0]]
                    land.append([x, y])
                    is_in_land = True
                    x += 1
            if not is_in_land:
                map[y][x] = count + 2
                count += 1
                land.append([x, y])
                x += 1
    return count


print(island(island_map))