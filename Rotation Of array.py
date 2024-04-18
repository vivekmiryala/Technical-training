def left_rotate(arr, d):
  n = len(arr)
  d %= n  
  return arr[d:] + arr[:d]
arr = [1, 2, 3, 4, 5]
d = 9
rotated_arr = left_rotate(arr, d)
print(rotated_arr)
