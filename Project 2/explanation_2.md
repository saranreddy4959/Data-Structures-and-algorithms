At, first i have taken an empty list next for the suffix i have initiated a variable and to that suffix i have added the path 

I have used os.listdir to print all the files in the directory using a for loop

Now,by checking each file or directory present in the parent directory it itreates now if it is a file and if that file ends with ".c" it appends the file path into a list.

Else, if not a file and a directory using recurion again i will do the same process so that it checks whether the file is present in that directory or it has another directory again . 

Time Complexity:So, as I am iterating through all the directions looking for a particular file if it is not present using recursion again I am iterating it to find the required file
Therefore it is a linear time Algorithm and Time Complexity is O(n)

Space Complexity:As, we are creating a empty list.So,the space complexity is O(n) where n is length of the list