def exist(board, word):
    """
    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
    :param board:
    :param word:
    :return:
    """
    if not board:
         return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if helper(board, i, j, word):
                    return True

    return False


def helper(board, word, i, j):  # Recursive process for DFS search

    if len(word) == 1:  # Reach the end, return True
        return True

    for next_start in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
        board[i][j] = None
        if 0 <= next_start[0] < len(board) and 0 <= next_start[1] < len(board[0]):
            if board[next_start[0]][next_start[1]] == word[1]:
                if helper(board, word[1:], next_start[0], next_start[1]):
                    return True
        board[i][j] = word[0]
    return False
