def high_and_low(arr: str )-> str:
    arr = arr.split(" ")
    new_arr=[]
    for i in arr:
        new_arr.append(int(i))
    for i in range(1, len(new_arr)):
        while new_arr[i-1] > new_arr[i] and i > 0:
            new_arr[i-1], new_arr[i] = new_arr[i], new_arr[i-1]
            i -= 1
    return f"{new_arr[-1]} {new_arr[0]}"
