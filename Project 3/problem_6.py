def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min=None
    max=None
    if not ints:
        return 
    for i in ints:
        if min is None and max is None:
            min=i
            max=i
        elif i<min:
            min=i
        elif i>max:
            max=i
    print(min,max)
    return (min,max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if((0,0)== get_min_max([0])) else "Fail")
print ("Pass" if (None == get_min_max([])) else "Fail")

"""
Output:
0 9
Pass
0 0
Pass
Pass
"""