def find_max(arr, index=0, now_max=float('-inf')):
    if index == len(arr)-1:
        return now_max
    
    if now_max < arr[index]:
        now_max = arr[index]
    
    if index < len(arr)-1:
        now_max = find_max(arr, index+1, now_max)

    return now_max


print(find_max([1,2,3,4,1]))
print(find_max([21,4,1]))
print(find_max([1,2,41,4,1,1,231,5,7,8,8,8]))