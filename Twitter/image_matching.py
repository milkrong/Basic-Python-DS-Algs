import os

def count_matches(grid1, grid2):
    grid1 = list(map(list))
    cnt = 0
    record1, record2 = [], []
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            record1 = bfs(grid1, i, j)
            record2 = bfs(grid2, i, j)
            if is_match(record1, record2):
                cnt += 1
    return cnt

def bfs(map, i, j):
    res = []
    if map[i][j] == 1:
        queue = []
        queue.insert(0, [i,j])
        while not queue == []:
            temp = []
            temp = queue.pop()
            r = temp[0]
            c = temp[1]
            map[r][c] = 0
            res.append(temp)
            if r-1 >=0 and c < len(map[r-1]) and map[r-1][c] == 1:
                queue.insert(0, [r-1,c])
            if r+1 < len(map) and c < len(map[r+1]) and map[r+1][c] == 1:
                queue.insert(0, [r+1,c])
            if c-1 >=0 and map[r][c-1] == 1:
                queue.insert(0, [r,c-1])
            if c+1 < len(map[r]) and map[r][c+1] ==1:
                queue.insert(0, [r,c+1])

    return res

def is_match(re1, re2):
    if len(re1) != len(re2):
        return False
    if len(re1) == 0:
        return False

    for i in range(len(re1)):
        if re1[i][0] != re2[i][0] or re1[i][1] != re2[i][1]:
            return False

    return True

if __name__ == '__main__':

    grid1_count = int(input().strip())

    grid1 = []

    for _ in range(grid1_count):
        grid1_item = input()
        grid1.append(grid1_item)

    grid2_count = int(input().strip())

    grid2 = []

    for _ in range(grid2_count):
        grid2_item = input()
        grid2.append(grid2_item)

    result = count_matches(grid1, grid2)

    print(result)