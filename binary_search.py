# binary_search.py

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
arr = [2, 4, 6, 8, 10]
target = 8
index = binary_search(arr, target)
if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found in the array")
