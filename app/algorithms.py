
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def qs(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)
        qs(arr, low, pIndex - 1)
        qs(arr, pIndex + 1, high)

def quick_sort(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list of integers")
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements in the list must be integers")

    qs(arr, 0, len(arr) - 1)
    return arr


def binary_search(arr, target):
    if not isinstance(arr, list) or not isinstance(target, int):
        raise ValueError("Input must be a list of integers and target must be an integer")

    arr.sort()
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def bfs(graph, start):
    if not isinstance(graph, dict) or not isinstance(start, str):
        raise ValueError("Graph must be a dictionary and start must be a string")

    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")

    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited
