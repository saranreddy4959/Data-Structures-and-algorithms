def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_pivot(input_list)
    if pivot == -1:
        return binary_search(input_list, 0, len(input_list)-1, number)
    if input_list[pivot] == number:
        return pivot
    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot, number)
    return binary_search(input_list, pivot+1, len(input_list)-1, number)
        
    
def binary_search(input_list, low, high, n):
    if high<low:
        return -1
    if high == low:
        return low
    mid = (low+high)//2
    if input_list[mid] == n:
        return mid
    elif input_list[mid] > n:
        return binary_search(input_list, low, mid-1, n)
    else:
        return binary_search(input_list, mid+1, high, n)
    
def find_pivot(input_list):
    mid = len(input_list)//2
    if len(input_list)==1:
        return -1
    if input_list[mid] > input_list[mid+1]:
        return mid
    if input_list[mid] < input_list[mid-1]:
        return (mid-1)
    if input_list[0]>=input_list[mid]:
        return (find_pivot(input_list[:mid]))
    return find_pivot(input_list[mid+1:])

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) #Pass
test_function([[7, 8, 1, 2, 3, 4, 6], 3])  #Pass