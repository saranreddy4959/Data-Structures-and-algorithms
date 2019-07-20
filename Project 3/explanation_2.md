First I would calculate the pivot point and divide the input list into 2 sub lists.
Now , call the binary search for the one of the two sub-lists
if an element is greater than the first element search in left input list
else, serach in the right input list
if an element is found in selected list then return its index else return -1

time complexity:O(logn)
Space Complexity:O(n)