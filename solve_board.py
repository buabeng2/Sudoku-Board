board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for index,current_array in enumerate(board):
        if index % 3 == 0 and index != 0:
            print("-----------------------")
        for index_in_current_array, current_value in enumerate(current_array):
            if (index_in_current_array % 3 == 0 and index_in_current_array != 0):
                print("|", end=" ")
            if (index_in_current_array == 8):
                print(current_value)
            else:
                print(str(current_value), end=" ")


print_board(board)