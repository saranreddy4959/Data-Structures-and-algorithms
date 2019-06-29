For the union and intersections of linked lists I have used the set data structures in python.
In the union I have taken one set and iterates the two linked lists by using the head and next values and appending each element into the set for a set as it is an unordered  collection I have use the sorted function to sort the elements in the set

Also, set does not store the duplicates it simply removes them 

For the intersection I have two sets  and added the two lists to two different sets now I will do the intersection of two sets using intersection method and appending them into a linked list 

Time Complexity: As, we are sorting the complete set so due this reason the complexity is O(nlogn)

Space Complexity :O(m+n) m for elements presents in the first set and n is the elements present in the second set as we are creating a new set for each of the linked lists its complexity is this 