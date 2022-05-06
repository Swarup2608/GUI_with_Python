def not_in_row(row,arr):
    st = set()
    for i in range(9):
        if arr[row][i] in st:
            return False
        else:
            st.add(arr[row][i])
    return True

def not_in_col(col,arr):
    st = set()
    for i in range(9):
        if arr[i][col] in st:
            return False
        else:
            st.add(arr[i][col])
    return True

def not_in_box(arr,row,col):
    st = set()
    for i in range(0,3):
        for j in range(0,3):
            curr = arr[i+row][col+j]
            if curr in st:
                return False
            else:
                st.add(curr)
    return True

def is_valid(arr,row,col):
    return (not_in_box(arr,row - row % 3,col - col % 3) and not_in_col(col,arr) and not_in_row(row,arr))

def is_config(arr,n):
    for i in range(0,n):
        for j in range(0,n):
            if not is_valid(arr,i,j):
                return False
    return True

board = []
for i in range(9):
    l = list(input().split())
    board.append(l)
if is_config(board,9):
    print("Valid")
else:
    print("inValid")