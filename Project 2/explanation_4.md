In this we have to find whether a element is present in the group or child or subchild.So,for that I have implemented the concept of recurion first I will check whether a element is present in the group if it is present it returns true else using recursion i will go the child and go through all the elements present in the child if it is present it return True.

So, the above process undergoes until an element is found if it is not found it returns false finally

Time Complexity:O(n) where n is the total number of elements present in that because for searching an element we are iterating all the available elements in that group

Space Complexity:O(1) as , because we are searching the elements present in that directory and we are not creating any new elements