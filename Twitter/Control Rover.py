def roverMove(matrixSize, cmds):
    matrix = [[y*matrixSize + x for x in range(matrixSize)] for y in range(matrixSize)]
    i, j = 0,0

    command_dict = {"RIGHT":[0,1],
                    "LEFT": [0,1],
                    "UP": [-1,0],
                    "DOWN": [1,0]}
    for command in cmds:
        command = command_dict[command]
        if i + command[0] < 0 or \
                i + command[0] > matrixSize - 1 or \
                j + command[1] < 0 or \
                j + command[1] > matrixSize - 1:
            continue
        else:
            i += command[0]
            j += command[1]

    return  matrix[i][j]

print(roverMove(4, ["RIGHT", "DOWN"]))