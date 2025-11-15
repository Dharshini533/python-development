arr = [4, 8, 15, 16, 23, 42]
x = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
        print(f"Element {x} found at index {mid}")
        found = True
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"Element {x} not found in the array")