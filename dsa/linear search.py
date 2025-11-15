arr = [4, 8, 15, 16, 23, 42]
x = int(input("Enter element to search: "))

found_index = -1

for i in range(len(arr)):
    if arr[i] == x:
        found_index = i
        break

if found_index != -1:
    print(f"Element {x} found at index {found_index}")
else:
    print(f"Element {x} not found in the array")