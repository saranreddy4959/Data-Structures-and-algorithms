def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    lst= sorted(input_list,reverse=True)
    str1=''
    str2=''
    for i in range(len(lst)):
        if i%2==0:
            str1=str1+str(lst[i])
        else:
            str2=str2+str(lst[i])
    return ([int(str1), int(str2)])

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]]) #Pass
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]] #Pass
test_function(test_case)
test_function([[4,5,8,9,3,2],[953,842]]) #Pass