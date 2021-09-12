
def swap(arr, left_pos, right_pos):
  temp = arr[left_pos]
  arr[left_pos] = arr[right_pos]
  arr[right_pos] = temp
 
def bubble_sort_unoptimized(arr):
  for itm in arr:
    for idx in range(len(arr) - 1):
      if arr[idx] > arr[idx + 1]:
        swap(arr, idx, idx + 1)

def bubble_sort(arr):
  iteration_count = 0
  for i in range(len(arr)):
    # iterate through unplaced elements
    for idx in range(len(arr) - i - 1):
      iteration_count += 1
      if arr[idx] > arr[idx + 1]:
        # replacement for swap function
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]